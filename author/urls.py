
from django.urls import path, include
from rest_framework import routers
from author.views import AuthorViewSet

# This is required when using namespace in include()
app_name = "author"

router = routers.DefaultRouter()
router.register("authors", AuthorViewSet, basename="author")

urlpatterns = [
    path("", include(router.urls)),
]
