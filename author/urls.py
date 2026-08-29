# Create your urls here
from django.urls import path, include
from rest_framework import routers

from author.views import AuthorViewSet


app_name = "authors"

router = routers.DefaultRouter()
router.register(r"authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]
