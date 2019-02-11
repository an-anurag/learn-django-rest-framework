from django.urls import path
from . import views
urlpatterns = [
    path('school-detail/', views.SchoolDetailAPIView.as_view(), name='school_detail')
]