from django.urls import path, include
from rest_framework import routers

from author.views import AuthorViewSet


router = routers.DefaultRouter()
router.register("authors", AuthorViewSet)

urlpatterns = [
    path("manage-list/", include(router.urls), name="manage-list"),
]

app_name = "author"
