from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Singer, Song, Album
from .serializers import SingerSerializer, AlbumSerializer, SongSerializer
from .permissions import IsOwnerOrReadOnly


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'singer']
    search_fields = ['name', 'singer']
    ordering_fields = ['name', 'singer', 'year_published']


class SingerList(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class SingerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'singer_slug'
    permission_classes = IsOwnerOrReadOnly,


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'album']
    search_fields = ['title', 'album']
    ordering_fields = ['title', 'album']


class AlbumSongList(SongList):
    filterset_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['title']

    def get_queryset(self):
        print(self.kwargs)
        return Song.objects.filter(album__slug=self.kwargs['album_slug'])


class SingerSongList(SongList):

    def get_queryset(self):
        print(self.kwargs)
        return Song.objects.filter(album__singer__slug=self.kwargs['singer_slug'])
