from django.urls import path

from author.views import AuthorViewSet


urlpatterns = [
    path("author/", AuthorViewSet.as_view(actions={
        "get": "list",
        "post": "create",
    }), name="manage-list"),
    path("author/<int:pk>/", AuthorViewSet.as_view(actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
    ), name="manage-detail"
    ),
]

app_name = "author"
