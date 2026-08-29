from django.urls import path
from rest_framework import routers
from .views import AuthorViewSet

urlpatterns = [
    path(
        "authors/",
        AuthorViewSet.as_view(
            {
                "get": "list",
                "post": "create",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="manage-list"
    ),
    path(
        "authors/<int:pk>/", AuthorViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        )
    ),
]

app_name = "author"
