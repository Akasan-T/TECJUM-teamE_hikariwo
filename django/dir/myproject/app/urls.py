# myapp/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    # ルートURLにアクセスすると index ビューを呼び出す
    path('', index, name='index'),
]