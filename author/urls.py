from django.urls import path, include
from rest_framework import routers

from author.views import AuthorViewSet


router = routers.DefaultRouter()
router.register("authors", AuthorViewSet, basename="manage")


urlpatterns = [
    path("", include(router.urls), name="author:manage-list"),
]

app_name = "author"
