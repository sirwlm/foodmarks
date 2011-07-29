from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
import json

from django.template import RequestContext

from foodmarks.fm.forms import *
from foodmarks.fm.models import *


def index(request):
    c = RequestContext(request)

    c['recipes'] = Recipe.objects.order_by('-time_created')[0:10]

    return render_to_response('index.html', c)


@login_required
def add_recipe(request):
    c = RequestContext(request)

    if request.POST:
        tags = json.loads(request.POST['tag-json'])

        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()

            ribbon = Ribbon(recipe=recipe, user=request.user)
            ribbon.save()
            
            for key in tags:
                for value in tags[key]['values']:
                    if value == '':
                        value = None
                        originalValue = None
                    else:
                        originalValue = tags[key]['values'][value]['original']
                    Tag(ribbon=ribbon,
                        key=key, 
                        originalKey=tags[key]['original'],
                        value=value,
                        originalValue=originalValue,
                        ).save()

            return redirect(reverse(my_recipes),
                            permanent=True)
        else:
            c['recipe_form'] = form
            return render_to_response('add_recipe.html', c)
    else:
        c['recipe_form'] = RecipeForm()

    return render_to_response('add_recipe.html', c)


@login_required
def my_recipes(request):
    c = RequestContext(request)
    c['ribbons'] = Ribbon.objects.filter( \
        user=request.user).select_related( \
        'recipe').order_by('-time_created')
    return render_to_response('my_recipes.html', c)


def recipe(request, recipe_id):
    c = RequestContext(request)
    
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except ObjectDoesNotExist:
        pass

    try:
        ribbon = Ribbon.objects.get(recipe=recipe,
                                    user=request.user)
    except ObjectDoesNotExist:
        pass

    c['recipe'] = recipe
    c['ribbon'] = ribbon

    return render_to_response('recipe.html', c)
