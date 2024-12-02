from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

app_name = "author"

router = DefaultRouter()
router.register("manage", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]
