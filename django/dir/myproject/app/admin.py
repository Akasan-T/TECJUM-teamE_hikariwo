# admin.py
from django.contrib import admin
from .models import Tab

class TabAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_displayed')
    list_editable = ('is_displayed',)
    # ※必要に応じて検索やフィルタリング機能も追加可能

admin.site.register(Tab, TabAdmin)
