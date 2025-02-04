# app/urls.py
from django.urls import path
from app import views

urlpatterns = [
    # タスク管理のトップページ（タスク一覧・追加）
    path('', views.index, name='index'),
    
    # ニュース記事の追加（フォーム専用）
    path('news/add/', views.add_news, name='add_news'),
    
    # ニュース記事の一覧表示
    path('news/', views.news_list, name='news_list'),
    
    # ニュース記事の作成（記事追加と編集で共通のフォームを利用）
    path('news/create/', views.news_create, name='news_create'),
    
    # ニュース記事の編集（記事ID(pk)に基づいて編集）
    path('news/edit/<int:pk>/', views.news_edit, name='news_edit'),
    
    # ニュース記事の削除（記事ID(pk)に基づいて削除）
    path('news/delete/<int:pk>/', views.news_delete, name='news_delete'),
    
    # URL入力から自動で記事情報を取得して表示するビュー
    path('news/auto-add/', views.auto_add_news, name='auto_add_news'),
]
