# forms.py
from django import forms
from .models import Tab

class TabForm(forms.ModelForm):
    class Meta:
        model = Tab
        fields = ['name', 'url', 'is_displayed']
