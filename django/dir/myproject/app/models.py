# models.py
from django.db import models
from django.core.exceptions import ValidationError

class Tab(models.Model):
    name = models.CharField("タブ名", max_length=100)
    url = models.CharField("リンク先URL", max_length=255, blank=True)
    is_displayed = models.BooleanField("サイトに表示する", default=False)

    def clean(self):
        """
        is_displayed を True にする場合、既に5個以上選択されていないかチェック。
        ※ 更新時は自身を除外する
        """
        if self.is_displayed:
            # 自身以外で表示中のタブ数をカウント
            active_count = Tab.objects.filter(is_displayed=True).exclude(pk=self.pk).count()
            if active_count >= 5:
                raise ValidationError("既に5個のタブが表示されています。")

    def save(self, *args, **kwargs):
        self.full_clean()  # clean() を呼んでバリデーションを実行
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
