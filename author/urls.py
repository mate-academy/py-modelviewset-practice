from django.urls import path, include
from rest_framework import routers

from author.views import AuthorViewSet

authors_router = routers.DefaultRouter()
authors_router.register("manage-list", AuthorViewSet, basename="manage")
urlpatterns = [
    path("", include(authors_router.urls))
]

app_name = "author"
