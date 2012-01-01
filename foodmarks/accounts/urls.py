from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^preferences/$', 'accounts.views.preferences'),
    url(r'^login/', 'django.contrib.auth.views.login',
        {'template_name': 'accounts/login.html'}),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/',}),

)


