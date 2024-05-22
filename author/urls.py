from rest_framework import routers
from django.urls import path, include
from .views import AuthorViewSet

app_name = "author"
router = routers.DefaultRouter()
router.register("", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]
