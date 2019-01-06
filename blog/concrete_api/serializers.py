from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'body',
            'publish',
            'status',
        )


class PostListSerializer(serializers.ModelSerializer, TaggitSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='blog_api:detail', lookup_field='slug')
    comments = TagListSerializerField()

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'author',
            'body',
            'comments',
            'publish',
            'created',
            'updated',
            'url',
        )


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'slug',
            'author',
            'body',
            'publish',
            'created',
            'updated',

        )


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Create and return a new user """
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],

        )

        user.set_password(validated_data['password'])
        user.save()

        return user
