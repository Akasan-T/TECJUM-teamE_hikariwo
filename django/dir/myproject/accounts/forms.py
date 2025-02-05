# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

# カスタムユーザー作成フォーム
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # モデルの定義に合わせて必要なフィールドを指定してください
        fields = ('username', 'email', 'name', 'furigana', 'age', 'gender')

# カスタム認証フォーム（ユーザー名またはメールアドレスで認証）
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "ユーザー名またはメールアドレス"

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            # メールアドレスとして認証を試みる
            if '@' in username:
                try:
                    user_obj = User.objects.get(email=username)
                    username = user_obj.username
                except User.DoesNotExist:
                    raise forms.ValidationError(
                        "ログインに失敗しました。正しいユーザー名またはパスワードを入力してください。",
                        code='invalid_login'
                    )
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "ログインに失敗しました。正しいユーザー名またはパスワードを入力してください。",
                    code='invalid_login'
                )
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
