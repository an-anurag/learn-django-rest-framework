from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_api_view, name='list'),
    path('posts/<int:id>/', views.post_api_view_detail, name='detail')
]