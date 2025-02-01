from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # ログインページへリダイレクト
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form})


from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    # 使用するテンプレートを指定します
    template_name = 'login.html'