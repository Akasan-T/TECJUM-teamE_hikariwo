# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField("メールアドレス", unique=True)
    name = models.CharField("名前", max_length=100, blank=True)
    furigana = models.CharField("フリガナ", max_length=100, blank=True)
    age = models.PositiveIntegerField("年齢", null=True, blank=True)
    
    GENDER_CHOICES = [
        ('M', '男性'),
        ('F', '女性'),
        ('O', 'その他'),
    ]
    # 通常は CharField として定義しますが、フォーム側で上書きします。
    gender = models.CharField("性別", max_length=2, choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return self.username
