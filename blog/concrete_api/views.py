from blog.models import Post
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import (AllowAny, IsAdminUser, IsAuthenticated)
from rest_framework.generics import (RetrieveUpdateAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView)
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .permissions import IsOwnerOrReadOnly
from .serializers import (PostListSerializer, PostDetailSerializer, PostCreateSerializer, AuthorSerializer)
from rest_framework.response import Response


class PostCreateAPIView(CreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostListAPIView(ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.published.all()
    serializer_class = PostCreateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(aurhor=self.request.user)


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.published.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.published.all()
    serializer_class = PostListSerializer
    permission_classes = (AllowAny,)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_class = (IsOwnerOrReadOnly, )
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('first_name', 'last_name')


class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, reqeust):
        """ Use the ObtainAuthToken APIView to validate and create a token"""
        return ObtainAuthToken().post(reqeust)
