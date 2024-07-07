from django.contrib import admin
from  . import  models
@admin.register(models.gorod)
class GorodAdmin(admin.ModelAdmin):
    list_display = ('City',)
    search_fields = ['City']


@admin.register(models.ulica)
class ulicaAdmin(admin.ModelAdmin):
    list_display = ('Street',)
    search_fields = ['Street']


@admin.register(models.magaz)
class MagazAdmin(admin.ModelAdmin):
    list_display = ('Shop',)
    search_fields = ['Shop']