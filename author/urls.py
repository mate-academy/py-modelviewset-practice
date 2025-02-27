from rest_framework import routers
from django.urls import include, path

from author.views import AuthorViewSet

router = routers.DefaultRouter()
router.register("authors", AuthorViewSet, basename="manage")

app_name = "author"

urlpatterns = [
    path("", include(router.urls))
]
