from django.urls import path, include
from rest_framework import routers

from author.views import AuthorViewSet

# router = routers.DefaultRouter()
# router.register("authors", AuthorViewSet)

author_list = AuthorViewSet.as_view(actions={
    "get": "list",
    "post": "create"
})

author_detail = AuthorViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy"
})

urlpatterns = [
    path("manage-list/", author_list, name="manage-list"),
    path("manage-list/<pk>/", author_detail, name="manage-detail"),
]

app_name = "author"
