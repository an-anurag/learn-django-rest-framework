from django.urls import path, include
from blog.concrete_api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('posts', views.PostViewSet)


app_name = 'blog_api'

urlpatterns = [
    path('list/', views.PostListAPIView.as_view(), name='list'),
    path('post/<slug:slug>/', views.PostDetailAPIView.as_view(), name='detail'),
    path('<slug:slug>/update/', views.PostUpdateAPIView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.PostDeleteAPIView.as_view(), name='delete'),
    path('post/create/', views.PostCreateAPIView.as_view(), name='create'),
    path('', include(router.urls))
]