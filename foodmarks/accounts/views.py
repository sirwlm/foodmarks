from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from foodmarks.accounts.forms import *
from foodmarks.accounts.models import *


def preferences(request):
    ctx = RequestContext(request)

    profile = request.user.get_profile()
    form = PreferencesForm(request.POST or None, instance=profile)

    if form.is_valid():
        form.save()

    ctx['form'] = form
    return render_to_response('accounts/preferences.html', ctx)
