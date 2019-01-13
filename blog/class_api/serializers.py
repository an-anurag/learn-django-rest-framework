from rest_framework import serializers
from rest_framework.utils.model_meta import _merge_fields_and_pk
from rest_framework.response import Response
from rest_framework import status

from ..models import Post, Movie, Song


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = (
            'id',
            'movie',
            'title',
            'composer',
            'duration',
        )

        # depth attribute for read only ie. for get
        # depth = 1


class MovieSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'name',
            'director',
            'rating',
            'year',
            'songs',
        )
        # depth = 1

    def create(self, validated_data):
        print(validated_data)
        songs = validated_data.pop('songs')
        movie = Movie.objects.create(**validated_data)
        print(songs)
        for song in songs:
            print(song)
            Song.objects.create(**song, movie_id=movie.id)
        return movie


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True, read_only=True)
    # url = serializers.HyperlinkedIdentityField(view_name='blog:detail', lookup_field='slug')

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'author',
            'body',
            'status',
            'comments',
            # 'url',

        )
