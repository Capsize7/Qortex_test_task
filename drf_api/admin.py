from django.contrib import admin
from .models import Album, Singer, Song
from django.contrib.admin import ModelAdmin


# Register your models here.
@admin.register(Singer)
class Singer(ModelAdmin):
    list_per_page = 5
    list_display = 'name', 'slug'
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Song)
class Song(ModelAdmin):
    list_per_page = 5
    list_display = 'title', 'album', 'slug'
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Album)
class Album(ModelAdmin):
    list_per_page = 5
    list_display = 'singer', 'year_published', 'slug'
    list_filter = ['singer']
    search_fields = ['singer']
