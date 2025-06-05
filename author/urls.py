from django.urls import path, include
from rest_framework import routers

from author.views import AuthorViewSet


app_name = "author"

author_urls = routers.DefaultRouter()
author_urls.register("authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(author_urls.urls))
]
