from django.urls import path

from author.views import AuthorViewSet

author_list = AuthorViewSet.as_view(
        actions={"get": "list", "post": "create"})

author_detail = AuthorViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "patch": "partial_update",
            "delete": "destroy",
        })

urlpatterns = [
    path("", author_list, name="manage-list"),
    path("<int:pk>/", author_detail, name="author-detail")
]

app_name = "author"
