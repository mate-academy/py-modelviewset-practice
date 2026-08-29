from django.urls import path, include
from rest_framework import routers

from .views import AuthorViewSet

app_name = "author"
router = routers.DefaultRouter()
router.register("authors", AuthorViewSet)
urlpatterns = [
    path("author/", AuthorViewSet.as_view({
        "get": "list",
        "post": "create"
    }), name="manage-list"),
    path("author/<int:pk>/", AuthorViewSet.as_view({
        "get": "retrieve",
        "delete": "destroy",
        "put": "update",
        "patch": "partial_update",
    }), name="manage-detail"),
]
