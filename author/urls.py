from django.urls import path

from author.views import AuthorViewSet

urlpatterns = [
    path(
        "manage-list/",
        AuthorViewSet.as_view(
            actions={
                "get": "list",
                "post": "create",
            }
        ),
        name="manage-list"
    ),
    path(
        "manage-list/<int:pk>/",
        AuthorViewSet.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="manage-detail"
    )
]

app_name = "author"
