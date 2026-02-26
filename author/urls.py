from author.views import AuthorViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = "author"

router = DefaultRouter()
router.register("authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]
