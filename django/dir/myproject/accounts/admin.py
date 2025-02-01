from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # 既に UserAdmin.fieldsets に email が含まれているため、追加フィールドには email を除外する
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name', 'furigana', 'gender', 'age')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name', 'furigana', 'gender', 'age')}),
    )
    list_display = ['username', 'email', 'name', 'gender', 'age']

admin.site.register(CustomUser, CustomUserAdmin)
