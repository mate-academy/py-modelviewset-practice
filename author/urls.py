from django.urls import path, include
from rest_framework import routers

from author import views

author_list = views.AuthorViewSet.as_view({
    "get": "list",
    "post": "create",
})

author_detail = views.AuthorViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})
urlpatterns = [
    path("manage/", author_list, name="manage-list"),
    path("manage/<int:pk>/", author_detail, name="manage-detail"),
]

app_name = "author"
