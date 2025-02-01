# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # 登録画面に表示するフィールド（password1, password2 は UserCreationForm に含まれる）
        fields = ('username', 'email', 'name', 'furigana', 'gender', 'age')
# accounts/forms.py（同ファイル内に追加）
from django.contrib.auth import authenticate, get_user_model

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ラベルを「ユーザー名またはメールアドレス」に変更
        self.fields['username'].label = "ユーザー名またはメールアドレス"

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            UserModel = get_user_model()
            # 入力値に「@」が含まれていればメールアドレスとしてユーザーを検索
            if '@' in username:
                try:
                    user_obj = UserModel.objects.get(email=username)
                    username = user_obj.username
                except UserModel.DoesNotExist:
                    # 該当するユーザーがなければ、そのまま認証を進めると後でエラーになる
                    pass
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
