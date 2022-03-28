from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('send', views.send, name="send"),
]
