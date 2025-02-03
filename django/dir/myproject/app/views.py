# myapp/views.py
from django.shortcuts import render, redirect

def index(request):
    """
    サイトのトップページをレンダリングするビューです。
    タブ情報は、コンテキストプロセッサ（myapp/context_processors.py）によって
    全テンプレートに自動的に渡されているため、ここでは単純にテンプレートをレンダリングします。
    """
    return render(request, 'index.html')

from .forms import TabForm

def add_tab(request):
    if request.method == 'POST':
        form = TabForm(request.POST)
        if form.is_valid():
            form.save()  # モデル側のバリデーションが実行される
            return redirect('index')
    else:
        form = TabForm()
    return render(request, 'myapp/add_tab.html', {'form': form})