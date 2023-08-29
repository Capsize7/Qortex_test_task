from django.urls import path
from .views import *

urlpatterns = [
    path('albums/', AlbumList.as_view()),
    path('albums/<slug:album_slug>/', AlbumSongList.as_view()),
    path('songs/', SongList.as_view()),
    path('songs/<slug:singer_slug>/', SingerSongList.as_view()),
    path('singers/', SingerList.as_view()),
    path('singers/<slug:singer_slug>', SingerDetail.as_view()),
]
