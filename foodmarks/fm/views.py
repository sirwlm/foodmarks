from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse

from foodmarks.fm.forms import *
from foodmarks.fm.models import *

def index(request):
    c = RequestContext(request)
    return render_to_response('index.html', c)

def add_recipe(request):
    c = RequestContext(request)

    if request.POST:
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return HttpResponse('Success!', c)
        else:
            c['recipe_form'] = form
            return render_to_response('add_recipe.html', c)
    else:
        c['recipe_form'] = RecipeForm()

    return render_to_response('add_recipe.html', c)
