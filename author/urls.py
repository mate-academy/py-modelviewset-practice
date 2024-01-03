# Create your urls here
from django.urls import path, include
from rest_framework import routers

from author.views import AuthorViewSet

router = routers.DefaultRouter()
router.register("author", AuthorViewSet)

urlpatterns = [
    path("", include(router.urls))
]
