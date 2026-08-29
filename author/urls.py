from rest_framework import routers
from author.views import AuthorViewSet
from django.urls import path, include


app_name = "author"

router = routers.DefaultRouter()

router.register(r"author", AuthorViewSet, basename="manage")
urlpatterns = [
    path("", include(router.urls)),
]
