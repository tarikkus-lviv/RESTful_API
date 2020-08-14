from django.contrib import admin
from django.urls import path, include

from .views import PostAPIView, DetailPostAPIView

urlpatterns = [
    path('<int:pk>/', DetailPostAPIView.as_view()),
    path('', PostAPIView.as_view()),
]
