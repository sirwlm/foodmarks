from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Q, Count
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.utils import simplejson

import json
import math

from foodmarks.fm.constants import *
from foodmarks.fm.forms import *
from foodmarks.fm.models import *

PAGE_SIZE = 10

class JsonResponse(HttpResponse):
    '''
    this class makes it easier to quickly turn content into json and return it as a response
    '''

    def __init__(self, content, mimetype="application/json", *args, **kwargs):
        if content:
            content = simplejson.dumps(content)
        else:
            content = simplejson.dumps({})
        super(JsonResponse, self).__init__(content, mimetype, *args, **kwargs)


def index(request):
    c = RequestContext(request)
    c['recipes'] = Recipe.objects.order_by('-time_created')[0:PAGE_SIZE]
    return render_to_response('index.html', c)


@login_required(login_url="/login/")
def bookmarklet(request):
    c = RequestContext(request)
    c['add'] = True
    saved = _save_recipe(request, c)

    if saved:
        return redirect(reverse(my_recipes), permanent=True)
    else:
        if request.method == 'GET':
            url = request.GET.get('url', None)
            if url:
                c['recipe_form'].initial['link'] = url
            title = request.GET.get('title', None)
            if title:
                c['recipe_form'].initial['title'] = title

        return render_to_response('bookmarklet.html', c)


@login_required(login_url="/login/")
def add_recipe(request):
    c = RequestContext(request)
    c['add'] = True
    saved = _save_recipe(request, c)

    if saved:
        return redirect(reverse(my_recipes), permanent=True)
    else:
        return render_to_response('edit_recipe.html', c)


def _save_recipe(request, c, ribbon=None, recipe=None):
    if request.user.is_staff:
        c['users'] = User.objects.all()
        c['user_id'] = request.user.id
        specified_user = request.user
        if request.POST:
            c['user_id'] = request.POST.get('user', request.user.id)
            try:
                specified_user = User.objects.get(id=c['user_id'])
            except ObjectDoesNotExist:
                pass

    c['known_values_to_keys'] = known_values_to_keys
    if ribbon and not recipe:
        recipe = ribbon.recipe

    recipe_form = RecipeForm(request.POST or None, prefix="re",
                             instance=recipe)
    ribbon_form = RibbonForm(request.POST or None, prefix="ri",
                             instance=ribbon)

    saved = False
    if recipe_form.is_valid() and ribbon_form.is_valid():
        recipe = recipe_form.save(commit=False)

        '''
        if recipe.link:
            other = Recipe.objects.filter(link=recipe.link)
            if other and other.id != recipe.id:
                recipe = RecipeForm(
                    request.POST, prefix="re", instance=other).save(
                    commit=False)
                    '''

        recipe.save()
        ribbon = ribbon_form.save(commit=False)
        ribbon.recipe = recipe
        if request.user.is_staff:
            ribbon.user = specified_user
        else:
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

@login_required(login_url="/login/")
def edit_recipe(request, ribbon_id):
    c = RequestContext(request)
    c['edit'] = True
    try:
        ribbon = Ribbon.objects.get(id=ribbon_id, user=request.user)
    except ObjectDoesNotExist:
        return redirect(reverse(my_recipes), permanent=True)

    saved = _save_recipe(request, c, ribbon)
    if saved:
        c['message'] = 'Recipe successfully saved.'
    return render_to_response('edit_recipe.html', c)


@login_required(login_url="/login/")
def my_recipes(request):
    c = RequestContext(request)
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
    else:
        page = 1
    c['ribbons'] = Ribbon.objects.filter(
        user=request.user)[(page - 1) * PAGE_SIZE: page * PAGE_SIZE
                           ].select_related('recipe')

    c['num_pages'] = int(math.ceil(
            Ribbon.objects.filter(user=request.user).count() / 10.0))
    c['page_range'] = xrange(1, c['num_pages'] + 1)
    c['page'] = page

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

        query_string = request.GET.get('q', '')
        if query_string != '':
            recipe_match_q = Q()

            query_tokens = query_string.split(' ')
            for token in query_tokens:
                if token:
                    recipe_match_q |= Q(recipe__title__icontains=token)
            c['q'] = query_string
            ribbons = ribbons.filter(recipe_match_q)

        c['own_ribbons'] = not all_ribbons
        selected_tags = request.GET.getlist('tag')
        if selected_tags:
            split_selected_tags = map(lambda s:s.split(':'), selected_tags)

            for split_selected_tag in split_selected_tags:
                ribbons = ribbons.filter(tag__key=split_selected_tag[0], tag__value=split_selected_tag[1])

        c['ribbons'] = ribbons

        tags = Tag.objects.filter(ribbon__in=ribbons).values('key', 'value').annotate(count=Count('value')).order_by('value')
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
    tags_ordered = []
    for key, values in tag_map.items():
        tags_ordered.append((key, sorted(values.values(),
                                         key=lambda a: a['priority']),))
    c['search_tags'] = sorted(tags_ordered, key=_get_key_order)


    return render_to_response('search.html', c)


@login_required(login_url="/login/")
def delete_ribbon(request, ribbon_id):
    try:
        ribbon = Ribbon.objects.get(id=ribbon_id, user=request.user)
    except ObjectDoesNotExist:
        return HttpResponse('ERROR', mimetype="application/json")
    recipe = ribbon.recipe
    ribbon.delete()
    if not recipe.ribbon_set.exists():
        recipe.delete();
    return HttpResponse('OK', mimetype="application/json")


@login_required(login_url="/login/")
def recipe_box(request):
    c = RequestContext(request)
    c['ribbons'] = Ribbon.objects.filter(
        user=request.user, is_boxed=True).select_related(
        'recipe').order_by('-time_created')
    return render_to_response('recipe_box.html', c)

@login_required(login_url="/login/")
def action(request):
    if not request.method == 'POST':
        return JsonResponse({'status':'OK'})
    action = request.POST.get('action', None)
    if action == 'changeBoxStatus':
        new_status = request.POST.get('newStatus', None) == 'true'
        recipe_id = request.POST.get('recipeId', None)
        ribbon_id = request.POST.get('ribbonId', None)
        if recipe_id:
            try:
                recipe = Recipe.objects.get(id=recipe_id)
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'FAIL'})
        else:
            return JsonResponse({'status': 'FAIL'})
        try:
            ribbon = Ribbon.objects.get(id=ribbon_id)
            if ribbon.recipe != recipe:
                return JsonResponse({'status': 'FAIL'})
        except ObjectDoesNotExist:
            ribbon = Ribbon(recipe=recipe, user=request.user)
        ribbon.is_boxed = new_status
        ribbon.save()

        return JsonResponse({'status': 'OK', 'ribbonId': ribbon.id})

    else:
        return JsonResponse({'status':'OK'})

@login_required(login_url="/login/")
def get_tag_category(request):
    if not request.method == 'GET':
        return JsonResponse({'status': 'OK'})
    value = request.GET.get('value', None)
    if not value:
        return JsonResponse({'status': 'OK', 'categories': ['']})
    seen_categories = set()
    categories = []

    users_tags = Tag.objects.filter(value=value, ribbon__user=request.user).values('key').annotate(count=Count('key')).order_by('-count')
    for tag in users_tags:
        categories.append(tag['key'])
        seen_categories.add(tag['key'])

    known_key = known_values_to_keys.get(value, None)
    if known_key and not known_key in seen_categories:
        categories.append(known_key)
        seen_categories.add(known_key)

    other_tags = Tag.objects.filter(value=value).values('key').annotate(count=Count('key')).order_by('-count')
    for tag in other_tags:
        if not tag['key'] in seen_categories:
            categories.append(tag['key'])
            seen_categories.add(tag['key'])

    return JsonResponse({'status': 'OK', 'categories': categories})
