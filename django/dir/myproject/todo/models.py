from django.conf import settings
from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        (3, '高'),   # 高 -> 3
        (2, '中'),   # 中 -> 2
        (1, '下'),   # 下 -> 1
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ユーザーごとにタスクを紐づけ
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)  # IntegerFieldに変更
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)  # 完了/未完了の状態
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    # 優先度を日本語表記で返す
    def get_priority_display(self):
        return dict(self.PRIORITY_CHOICES).get(self.priority)
