# models.py
from django.db import models

# --------------------------------------------------
# スクレイピング対象のサイト情報を管理するモデル
# --------------------------------------------------
class ScrapingTarget(models.Model):
    url = models.URLField(unique=True, verbose_name="サイトURL")
    site_name = models.CharField(max_length=100, verbose_name="サイト名")
    selector = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="スクレイピングセレクタ"
    )

    def __str__(self):
        return self.site_name

# --------------------------------------------------
# 10種類の分類（カテゴリ）の選択肢例
# --------------------------------------------------
NEWS_CATEGORY_CHOICES = [
    ('cat1', 'Category 1'),
    ('cat2', 'Category 2'),
    ('cat3', 'Category 3'),
    ('cat4', 'Category 4'),
    ('cat5', 'Category 5'),
    ('cat6', 'Category 6'),
    ('cat7', 'Category 7'),
    ('cat8', 'Category 8'),
    ('cat9', 'Category 9'),
    ('cat10', 'Category 10'),
]

# --------------------------------------------------
# ニュース記事（実際に収集・保存した記事）のモデル（固定のカテゴリを利用）
# --------------------------------------------------
class NewsArticle(models.Model):
    title = models.CharField(max_length=255, verbose_name="タイトル")
    content = models.TextField(verbose_name="本文")
    source_url = models.URLField("元記事URL", blank=True, null=True)  # 追加
    category = models.CharField(
        max_length=10,
        choices=NEWS_CATEGORY_CHOICES,
        default='cat1',
        verbose_name="カテゴリ"
    )
    image = models.ImageField(
        upload_to='news_images/',
        blank=True,
        null=True,
        verbose_name="記事画像"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "ニュース記事"
        verbose_name_plural = "ニュース記事一覧"
    
    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"
