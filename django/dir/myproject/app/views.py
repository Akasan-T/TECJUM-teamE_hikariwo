from todo.models import Task
from todo.forms import TaskForm
from app.forms import NewsArticleForm, AutoNewsArticleForm
from app.models import NewsArticle, NEWS_CATEGORY_CHOICES
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
from django.shortcuts import render, get_object_or_404, redirect
def index(request):
    # タスクの一覧を作成日時の降順で取得
    tasks = Task.objects.all().order_by('-created_at')
    
    # POSTリクエストの場合、タスクフォームから新規タスクを作成
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    
    # ニュース記事の一覧を作成日時の降順で取得
    articles = NewsArticle.objects.all().order_by('category', '-created_at')
    # 新着記事トップ3を抽出
    newest_articles = articles[:3]
    # NEWS_CATEGORY_CHOICES（固定のカテゴリ選択肢）の辞書を作成（キー→表示名）
    category_map = dict(NEWS_CATEGORY_CHOICES)
    
    # コンテキストにタスク、フォーム、ニュース記事、最新記事、カテゴリのマッピングをまとめる
    context = {
        'tasks': tasks,
        'form': form,
        'articles': articles,
        'newest_articles': newest_articles,
        'category_map': category_map,
    }
    
    return render(request, 'index.html', context)

def add_news(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # 保存後はニュース一覧ページなどへリダイレクトする例です
            return redirect('news_list')  # 'news_list' は適宜、一覧表示用の URL 名に変更してください
    else:
        form = NewsArticleForm()
    
    context = {
        'form': form,
    }
    return render(request, 'add_news.html', context)


def news_list(request):
    articles = NewsArticle.objects.all().order_by('-created_at')
    context = {'articles': articles}
    return render(request, 'news_list.html', context)

def news_create(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsArticleForm()
    return render(request, 'news_form.html', {'form': form, 'action': '追加'})

# app/views.py
def news_edit(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsArticleForm(instance=article)
    return render(request, 'news_form.html', {'form': form, 'action': '編集'})


# app/views.py
def news_delete(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('news_list')
    return render(request, 'news_confirm_delete.html', {'article': article})

def auto_add_news(request):
    """
    ユーザーが入力した URL から外部ページのタイトル、画像、元記事のURLを取得し、
    記事を自動作成して保存するビュー
    """
    error_message = None
    if request.method == 'POST':
        form = AutoNewsArticleForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
            except requests.RequestException as e:
                error_message = f"URL の取得に失敗しました: {e}"
            else:
                # BeautifulSoup を用いて HTML をパース
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # タイトル取得：<meta property="og:title"> を優先、なければ <title> タグ
                meta_title = soup.find("meta", property="og:title")
                if meta_title and meta_title.get("content"):
                    title = meta_title["content"]
                else:
                    title = soup.title.string.strip() if soup.title else "タイトル不明"
                
                # 画像URL取得：<meta property="og:image"> を優先、なければ最初の <img> タグ
                meta_image = soup.find("meta", property="og:image")
                if meta_image and meta_image.get("content"):
                    image_url = meta_image["content"]
                else:
                    first_img = soup.find("img")
                    if first_img and first_img.has_attr("src"):
                        image_url = urljoin(url, first_img["src"])
                    else:
                        image_url = None

                # 元記事URL取得：<meta property="og:url"> を優先、なければユーザー入力の URL を利用
                meta_url = soup.find("meta", property="og:url")
                if meta_url and meta_url.get("content"):
                    source_url = meta_url["content"]
                else:
                    source_url = url

                # NewsArticle インスタンスを作成して保存する
                article = NewsArticle.objects.create(
                    title=title,
                    content=f"元記事: {url}",
                    source_url=source_url,  # 取得した元記事URLを保存
                    category='cat1',       # 固定の選択肢から設定（必要に応じて変更）
                )
                
                # 画像が取得できた場合は、画像フィールドに保存する処理
                if image_url:
                    try:
                        img_response = requests.get(image_url, timeout=10)
                        img_response.raise_for_status()
                        from django.core.files.base import ContentFile
                        import os
                        file_name = os.path.basename(image_url)
                        article.image.save(file_name, ContentFile(img_response.content), save=True)
                    except requests.RequestException:
                        pass

                return redirect('news_list')
    else:
        form = AutoNewsArticleForm()
    
    context = {
        'form': form,
        'error_message': error_message,
    }
    return render(request, 'auto_add_news.html', context)
