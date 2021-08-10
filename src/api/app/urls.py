from django.urls import path
from . import views

urlpatterns = [
    path('questions', views.AppView.as_view(), name='questions')
]
