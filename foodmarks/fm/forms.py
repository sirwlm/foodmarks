from django import forms
from django.forms import ModelForm

from foodmarks.fm.models import *

class RecipeForm(ModelForm):

    class Meta:
        model = Recipe

        widgets = {
                'title': forms.TextInput(attrs={'size': '50'}),
                'link': forms.TextInput(attrs={'size': '50'})
                }


class RibbonForm(ModelForm):

    class Meta:
        model = Ribbon
        exclude = ('recipe', 'user', 'boxed_on')
