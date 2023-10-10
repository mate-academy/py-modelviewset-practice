from django.urls import include, path
from rest_framework.routers import SimpleRouter

from author.views import AuthorViewSet


router = SimpleRouter()
router.register("authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "authors"
