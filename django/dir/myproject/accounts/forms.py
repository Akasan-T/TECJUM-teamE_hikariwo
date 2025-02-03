# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

# カスタムユーザー作成フォーム
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # モデルに合わせて必要なフィールドを指定してください
        fields = ('username', 'email', 'name', 'furigana', 'age', 'gender')

# カスタム認証フォーム（ユーザー名またはメールアドレスで認証）
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ラベルを変更しておくなどのカスタマイズ
        self.fields['username'].label = "ユーザー名またはメールアドレス"

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            # 入力に '@' が含まれているならメールアドレスとしてユーザーを検索
            if '@' in username:
                try:
                    user_obj = User.objects.get(email=username)
                    username = user_obj.username
                except User.DoesNotExist:
                    pass  # 該当ユーザーがなければそのまま進む（後で認証エラーになる）
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
