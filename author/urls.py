from django.urls import path
from author.views import AuthorViewsSet

author_list = AuthorViewsSet.as_view(actions={
    "get": "list",
    "post": "create"
})
author_detail = AuthorViewsSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})


urlpatterns = [
    path("author/", author_list, name="manage-list"),
    path("author/<int:pk>/", author_detail, name="manage-detail"),
]

app_name = "author"
