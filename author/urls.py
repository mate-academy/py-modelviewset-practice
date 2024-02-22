from django.urls import path
from author.views import AuthorViewSet


app_name = "author"

urlpatterns = [
    path("authors/", AuthorViewSet.as_view(
        {"get": "list", "post": "create"}), name="manage-list"),
    path("authors/<int:pk>/", AuthorViewSet.as_view(
        {"get": "retrieve", "put": "update",
         "patch": "partial_update", "delete":
             "destroy"}), name="author-detail"),
]