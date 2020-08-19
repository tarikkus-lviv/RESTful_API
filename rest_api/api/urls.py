from django.contrib import admin
from django.urls import path, include

from .views import PostAPIView, DetailPostAPIView, PostLikeAPIToggle

urlpatterns = [
    path('<int:pk>/like/', PostLikeAPIToggle.as_view()),
    # path('', include('likes.api.urls')),
    path('<int:pk>/', DetailPostAPIView.as_view()),
    path('', PostAPIView.as_view()),
]
