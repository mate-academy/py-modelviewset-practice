# Create your urls here
from django.urls import path

from author.serializers import AuthorViewSet

urlpatterns = [
    path(
        "authors/",
        AuthorViewSet.as_view(
            {"get": "list", "post": "create"}
        ),
        name="manage-list"
    ),
    path(
        "authors/<int:pk>/",
        AuthorViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="author-detail"
    ),
]

app_name = "author"
