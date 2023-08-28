from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from drf_api.models import Song, Singer, Album


class SingerSerializer(ModelSerializer):
    class Meta:
        model = Singer
        fields = 'name',


class SongSerializer(ModelSerializer):

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['album'] = instance.album.name
        return rep

    class Meta:
        model = Song
        fields = 'title', 'album'


class AlbumSerializer(ModelSerializer):

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['singer'] = instance.singer.name
        return rep

    class Meta:
        model = Album
        fields = 'name', 'singer', 'year_published'


