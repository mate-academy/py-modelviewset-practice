from rest_framework import routers
from django.urls import path, include
from author.views import AuthorViewSet

routers = routers.DefaultRouter()
routers.register("authors", AuthorViewSet, basename="manage")

urlpatterns = [path("", include(routers.urls))]

app_name = "author"
