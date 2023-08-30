from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import *

urlpatterns = [
    path('albums/', AlbumList.as_view(), name='albums'),
    path('albums/<slug:album_slug>/', AlbumSongList.as_view(), name='albums_songs'),
    path('songs/', SongList.as_view(), name='songs'),
    path('songs/<slug:singer_slug>/', SingerSongList.as_view(), name='singer_songs'),
    path('singers/', SingerList.as_view(), name='singers'),
    path('singers/<slug:singer_slug>', SingerDetail.as_view(), name='singer_detail'),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger")
]
