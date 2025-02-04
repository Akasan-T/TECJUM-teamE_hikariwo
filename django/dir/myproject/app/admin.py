# app/admin.py
from django.contrib import admin
from app.models import  ScrapingTarget, NewsArticle


class TabAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'is_displayed')
    list_filter = ('is_displayed',)
    search_fields = ('name', 'url')

@admin.register(ScrapingTarget)
class ScrapingTargetAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'url', 'selector')
    search_fields = ('site_name', 'url')

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')
