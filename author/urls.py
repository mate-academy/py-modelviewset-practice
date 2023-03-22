from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet


author_router = routers.DefaultRouter()
author_router.register("authors", AuthorViewSet, basename="manage")


urlpatterns = [path("", include(author_router.urls))]

app_name = "author"
