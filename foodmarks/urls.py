from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from foodmarks.fm.feeds import NewestRecipesFeed

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^add/', 'fm.views.add_recipe'),
    url(r'^action/', 'fm.views.action'),
    url(r'^bookmarklet/', 'fm.views.bookmarklet'),
    url(r'^edit/(\d+)/$', 'fm.views.edit_recipe'),
    url(r'^recipebox/', 'fm.views.recipe_box'),
    url(r'^myrecipes/', 'fm.views.my_recipes'),
    url(r'^recipe/(\d+)/$', 'fm.views.view_recipe'),
    url(r'^ribbon/delete/(\d+)/$', 'fm.views.delete_ribbon'),
    url(r'^search/$', 'fm.views.search_recipes'),
    url(r'^tag/category/$', 'fm.views.get_tag_category'),
    url(r'^feed/$', NewestRecipesFeed()),
    url(r'^$', 'fm.views.index', name='index'),
    # url(r'^foodmarks/', include('foodmarks.foo.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += staticfiles_urlpatterns()
