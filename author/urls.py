# Create your urls here
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from author.views import AuthorViewSet

router = DefaultRouter()
router.register(r"manage", AuthorViewSet, basename="manage")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]

app_name = "author"
