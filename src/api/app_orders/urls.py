from django.urls import path
from . import views


urlpatterns = [
    path('orders', views.AppOrdersView.as_view()),
]
