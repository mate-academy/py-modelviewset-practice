from django.urls import path, include

from author.views import AuthorViewSet


author_list = AuthorViewSet.as_view({"get": "list", "post": "create"})
author_detail = AuthorViewSet.as_view(
    {"get": "retrieve",
     "put": "update",
     "delete": "destroy",
     "patch": "partial_update"}
)


urlpatterns = [
    path("authors/", author_list, name="manage-list"),
    path("authors/<int:pk>/", author_detail, name="manage-detail"),
]

app_name = "author"
