# Create your urls here
from django.urls import path

from author.views import AuthorViewSet

author_list = AuthorViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
author_detail = AuthorViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

app_name = "author"

urlpatterns = [
    path("authors/", author_list, name="manage-list"),
    path("authors/<int:pk>/", author_detail, name="manage-detail"),
]
