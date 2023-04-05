from django.urls import path

from author.views import AuthorViewSet


urlpatterns = [
    path("authors/", AuthorViewSet.as_view(actions={
        "get": "list",
        "post": "create"
        }), name="manage-list"),
    path("authors/<int:pk>/", AuthorViewSet.as_view(
        actions={
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        }), name="manage-detail"),
]

app_name = "author"
