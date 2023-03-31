from django.urls import path, include

from rest_framework import routers

from .views import AuthorViewSet

routers = routers.DefaultRouter()
routers.register("authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(routers.urls)),
]

app_name = "author"
