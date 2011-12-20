from django import forms
from django.forms import ModelForm

from foodmarks.fm.models import *

class RecipeForm(ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'size': '50'}))
    link = forms.URLField(
        max_length=256, verify_exists=True,
        widget=forms.TextInput(attrs={'size': '50'}))
    class Meta:
        model = Recipe


class RibbonForm(ModelForm):
    class Meta:
        model = Ribbon
        exclude = ('recipe', 'user', 'is_boxed', 'is_used', 'thumb', )

