from django.urls import path
from . import views


urlpatterns = [
    path('questions', views.AppView.as_view(), name='questions'),
    path('questions/generic', views.QuestionAPIView.as_view())
]
