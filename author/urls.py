from django.urls import path, include

from rest_framework import routers

from .views import AuthorViewSet

manage_list = AuthorViewSet.as_view(actions={"get": "list", "post": "create"})
manage_detail = AuthorViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("authors/", manage_list, name="manage-list"),
    path("authors/<int:pk>/", manage_detail, name="manage-detail")
]

app_name = "author"
