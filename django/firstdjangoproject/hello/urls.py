from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path("", views.index, name="index"), # an empty path url with view.py file and name of function define as index and a string name as index
    path("himan", views.himan, name="himan")
]