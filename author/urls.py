from django.urls import path

from author.views import AuthorViewSet

app_name = "author"

author_list = AuthorViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

author_detail = AuthorViewSet.as_view(actions={
    "get": "retrieve",
    "post": "update",
    "put": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("authors/", author_list, name="author_list"),
    path("authors/<int:pk>", author_detail, name="author_detail"),
]
