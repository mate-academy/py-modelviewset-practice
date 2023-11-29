from django.urls import path, include
from rest_framework.routers import DefaultRouter

from author.views import AuthorViewSet

router = DefaultRouter()
router.register("authors", AuthorViewSet, "manage")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "author"
