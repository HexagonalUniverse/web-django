
from django.urls import path, URLPattern

from . import views


urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
]
