from django.urls import path, include

from author.views import AuthorViewSet


author_list = AuthorViewSet.as_view(actions={
    "get": "list",
    "post": "create",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"}
)

author_detail = AuthorViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"}
)


urlpatterns = [
    path("authors/", author_list, name="author-list"),
    path("authors/<int:pk>/", author_detail, name="author-detail"),
]

app_name = "author"
