
# app/forms.py
from django import forms
from app.models import NewsArticle



# app/forms.py

class AutoNewsArticleForm(forms.Form):
    url = forms.URLField(label="記事URL", help_text="記事のURLを入力してください")



class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'content', 'category', 'image']