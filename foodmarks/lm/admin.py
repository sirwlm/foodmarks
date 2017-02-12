from models import *
from django.contrib import admin

class LiquidRecipesAdmin(admin.ModelAdmin):
    search_fields = ('recipename', 'recipeauthor', 'rating', 'flv1', 'flvm1', )


class LiquidFlavorsAdmin(admin.ModelAdmin):
    search_fields = ('name', 'flvm', 'flvnotes', 'rating', )


class RibbonAdmin(admin.ModelAdmin):
    search_fields = ('recipename', 'recipeauthor', 'rating' )
    list_display = ('id', 'recipename', 'user', 'flv1', 'flvm1', )
    list_filter = ('user', 'flv1', 'flvm1',  )
    raw_id_fields = ('recipename', 'user')


class TagAdmin(admin.ModelAdmin):
    search_fields = ('key', 'value', )
    list_display = ('key', 'value', 'ribbon', )
    list_filter = ('key', )
    raw_id_fields = ('ribbon', )

admin.site.register(LiquidRecipes, LiquidRecipesAdmin)
admin.site.register(LiquidFlavors, LiquidFlavorsAdmin)
admin.site.register(Ribbon, RibbonAdmin)
admin.site.register(Tag, TagAdmin)
