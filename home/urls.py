
from django.urls import path, URLPattern

from . import views


urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),

    # trem novo
    path("sobre/", views.sobre, name="sobre"),
]
