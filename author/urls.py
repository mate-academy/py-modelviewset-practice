from django.urls import path, include
from rest_framework.routers import DefaultRouter

from author.views import AuthorViewSet

app_name = "author"

router = DefaultRouter()
router.register(r"author", AuthorViewSet, basename="authors")

urlpatterns = [
    path("", include(router.urls)),
]
