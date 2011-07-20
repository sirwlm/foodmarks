from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^add/', 'fm.views.add_recipe'),
    url(r'^myrecipes/', 'fm.views.my_recipes'),
    url(r'^recipe/(\d+)/$', 'fm.views.recipe'),                       
    url(r'^$', 'fm.views.index', name='index'),
    # url(r'^foodmarks/', include('foodmarks.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^logout/', 'django.contrib.auth.views.logout',
        {'next_page': '/',}),
)

urlpatterns += staticfiles_urlpatterns()
