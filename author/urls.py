from django.urls import include, path
from rest_framework import routers

from author.views import AuthorViewSet


router = routers.DefaultRouter()
router.register("author", AuthorViewSet)

urlpatterns = [
    path("", include((router.urls, "author"), namespace="manage-list"))
]


app_name = "authors"
