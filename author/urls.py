from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet

app_name = "author"
router = DefaultRouter()
router.register(r"authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),  # Include the router's URLs
]
