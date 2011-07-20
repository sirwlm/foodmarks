from django import forms
from django.forms import ModelForm

from foodmarks.fm.models import *

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
