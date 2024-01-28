from django.urls import include, path
from rest_framework import routers

from author.views import AuthorList, AuthorDetail


urlpatterns = [
    path("author/", AuthorList.as_view(), name="manage-list"),
    path("author/<int:pk>/", AuthorDetail.as_view(), name="manage-detail"),
]


app_name = "author"
