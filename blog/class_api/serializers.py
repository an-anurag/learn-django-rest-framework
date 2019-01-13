from rest_framework import serializers
from rest_framework.utils.model_meta import _merge_fields_and_pk
from rest_framework.response import Response
from rest_framework import status

from ..models import Post, Movie, Song


class SongSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Song
        fields = (
            'id',
            'movie',
            'title',
            'composer',
            'duration',
        )

        # create got multiple keyword argument for movie TypeError
        read_only_fields = ('movie',)
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
        # validated data is dict
        print(validated_data)
        # pop song because it is not a field of movie
        songs = validated_data.pop('songs')
        # create a movie object
        movie = Movie.objects.create(**validated_data)
        # songs is ordered dict list
        print(songs)
        for song in songs:
            print(song)
            # pick a each dict then create song object associated with movie created earlier

            # create got multiple keyword argument for movie TypeError (read_only_fields)
            # movie_id=movie.id
            Song.objects.create(**song, movie_id=movie.id)
        return movie

    def update(self, instance, validated_data):
        # validated data is dict
        print(validated_data)
        # pop song because it is not a field of movie
        songs = validated_data.pop('songs')
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        keep_songs = []
        existing_ids = [song.id for song in instance.songs]
        for song in songs:
            if 'id' in song.keys():
                if Song.objects.filter(id=song['id']).exists():
                    s = Song.objects.get(id=song['id'])
                    s.title = song.get('title', song.title)
                    s.save()
                    keep_songs.append(song.id)
                else:
                    continue
            else:
                s = Song.objects.create(**song, movie=instance)
                keep_songs.append(s.id)
        
        for song in instance.songs:
            if song.id not in keep_songs:
                song.delete()
        return instance


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
