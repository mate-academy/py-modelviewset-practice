from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from author.views import AuthorViewSet

router = routers.DefaultRouter()
router.register("manage", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "author"
