from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.PostAPIView.as_view(), name='list'),
    path('posts/<int:id>/', views.PostDetailView.as_view(), name='detail'),
    path('movies/', views.MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:id>/', views.MovieDetailAPIView.as_view(), name='movie_detail'),
    path('songs/', views.SongAPIView.as_view(), name='song_list'),

]
