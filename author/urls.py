from django.urls import path, include
from rest_framework import routers

from .views import AuthorViewSet


app_name = "author"

router = routers.SimpleRouter()
router.register(r"authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]
