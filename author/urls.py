from django.urls import path, include
from rest_framework import routers

from author.views import AuthorViewSet

author_router = routers.SimpleRouter()
author_router.register("authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(author_router.urls))
]


app_name = "author"
