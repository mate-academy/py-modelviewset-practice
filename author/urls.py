from rest_framework import routers
from django.urls import path, include

from author.views import AuthorViewSet

app_name = "author"


router = routers.DefaultRouter()
router.register("authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]
