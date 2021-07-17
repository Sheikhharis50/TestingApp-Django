from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app'),
    path('questions', views.AppView.as_view(), name='questions')
]
