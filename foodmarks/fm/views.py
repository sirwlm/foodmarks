from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Q, Count
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
    c['add'] = True
    '''
    c['known_values_to_keys'] = known_values_to_keys

    if request.POST:
        tags = json.loads(request.POST['tag-json'])

        recipe_form = RecipeForm(request.POST, prefix="re")
        ribbon_form = RibbonForm(request.POST, prefix="ri")
        if recipe_form.is_valid() and ribbon_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.save()

            ribbon = ribbon_form.save(commit=False)
            ribbon.recipe = recipe
            ribbon.user = request.user
            ribbon.save()

            for key in tags:
                for value in tags[key]:
                    if value == '':
                        value = None
                    Tag(ribbon=ribbon, key=key, value=value).save()

            return redirect(reverse(my_recipes), permanent=True)
        else:
            c['recipe_form'] = recipe_form
            c['ribbon_form'] = ribbon_form
            c['tags'] = tags
            return render_to_response('edit_recipe.html', c)
    else:
        c['recipe_form'] = RecipeForm(prefix="re")
        c['ribbon_form'] = RibbonForm(prefix="ri")
        '''
    saved = _save_recipe(request, c)
    if saved:
        return redirect(reverse(my_recipes), permanent=True)
    else:
        return render_to_response('edit_recipe.html', c)


def _save_recipe(request, c, ribbon=None):
    c['known_values_to_keys'] = known_values_to_keys
    if ribbon:
        recipe = ribbon.recipe
    else:
        recipe = None

    recipe_form = RecipeForm(request.POST or None, prefix="re",
                             instance=recipe)
    ribbon_form = RibbonForm(request.POST or None, prefix="ri",
                             instance=ribbon)

    saved = False
    if recipe_form.is_valid() and ribbon_form.is_valid():
        recipe = recipe_form.save(commit=False)
        recipe.save()
        ribbon = ribbon_form.save(commit=False)
        ribbon.recipe = recipe
        ribbon.user = request.user
        ribbon.save()

        if request.POST:
            tags = json.loads(request.POST['tag-json'])
            for key in tags:
                for value in tags[key]:
                    if value == '':
                        value = None
                    if tags[key][value].get('id', False):
                        tag = Tag.objects.get(id=tags[key][value]['id'])
                        if tags[key][value].get('deleted', False):
                            tag.delete()
                    elif not tags[key][value].get('deleted', False):
                        Tag(ribbon=ribbon, key=key, value=value).save()
        saved = True
    else:
        tags = {}
        if ribbon:
            actual_tags = ribbon.tag_set.all()
            for actual_tag in actual_tags:
                if not actual_tag.key in tags:
                    tags[actual_tag.key] = {}
                tags[actual_tag.key][actual_tag.value] = \
                    {'id': actual_tag.id}
    c['recipe_form'] = recipe_form
    c['ribbon_form'] = ribbon_form
    c['ribbon'] = ribbon
    c['recipe'] = recipe
    c['tags'] = tags
    return saved

@login_required
def edit_recipe(request, ribbon_id):
    c = RequestContext(request)
    c['edit'] = True
    try:
        ribbon = Ribbon.objects.get(id=ribbon_id, user=request.user)
    except ObjectDoesNotExist:
        return redirect(reverse(my_recipes), permanent=True)

    _save_recipe(request, c, ribbon)

    return render_to_response('edit_recipe.html', c)


@login_required(login_url="/login/")
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

    if request.user.is_authenticated():
        try:
            ribbon = Ribbon.objects.get(recipe=recipe, user=request.user)
            c['ribbon'] = ribbon
        except ObjectDoesNotExist:
            pass

    c['recipe'] = recipe

    return render_to_response('recipe.html', c)


def _get_key_order(val):
    key = val[0]
    try:
        index = ordered_known_keys.index(key)
        return '{0: 3d}'.format(index)
    except ValueError:
        return '{0: 3d}{1}'.format(len(ordered_known_keys), key)


def search_recipes(request):
    c = RequestContext(request)

    if request.method == 'GET':
        all_ribbons = request.GET.get('all', False) or \
            not request.user.is_authenticated()
        if all_ribbons:
            ribbons = Ribbon.objects.all()
        else:
            ribbons = Ribbon.objects.filter(user=request.user)

        c['own_ribbons'] = not all_ribbons
        print c['own_ribbons']
        selected_tags = request.GET.getlist('tag')
        if selected_tags:
            split_selected_tags = map(lambda s:s.split(':'), selected_tags)

            for split_selected_tag in split_selected_tags:
                ribbons = ribbons.filter(tag__key=split_selected_tag[0], tag__value=split_selected_tag[1])

        c['ribbons'] = ribbons

        tags = Tag.objects.filter(ribbon__in=ribbons).values('key', 'value').annotate(count=Count('value')).order_by('-count')
        tag_map = {}
        priority = 0
        for tag in tags:
            if not tag['key'] in tag_map:
                tag_map[tag['key']] = {}
            value = {'value': tag['value'], 'count': tag['count'],
                     'priority': priority}
            if tag['key'] + ':' + tag['value'] in selected_tags:
                value['selected'] = True
            tag_map[tag['key']][tag['value']] = value
            priority += 1

        if all_ribbons:
            c['recipes'] = Recipe.objects.filter(ribbon__in=ribbons)

        '''
                tag_map[split_selected_tag[0]][split_selected_tag[1]]['selected'] = True
                '''
        '''
        query_string = request.GET.get('q', '')
        if query_string != '':

            recipe_match_q = Q()
            ribbon_match_q = Q()

            query_tokens = query_string.split(' ')
            for token in tokens:
                recipe_match_q |= Q(title__icontains=token) | \
                    Q(description__icontains=token) | \
                    Q(ingredients__icontains=token) | \
                    Q(directions__icontains=token) | \
                    Q(link__icontains=token)
                if request.user.is_authenticated:
                    ribbon_match_q = Q(ribbon__comments__icontains=token,
                                       ribbon__user=request.user)
                                       '''
    tags_ordered = []
    for key, values in tag_map.items():
        tags_ordered.append((key, sorted(values.values(),
                                         key=lambda a: a['priority']),))
    c['search_tags'] = sorted(tags_ordered, key=_get_key_order)


    return render_to_response('search.html', c)
