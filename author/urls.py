from django.urls import path, include
from rest_framework import routers

from author.views import AuthorViewSet

manage_router = routers.DefaultRouter()
manage_router.register("authors", AuthorViewSet, basename="manage")

app_name = "author"
urlpatterns = [
    path("", include(manage_router.urls)),
]
