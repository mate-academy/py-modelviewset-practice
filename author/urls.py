from django.urls import include, path
from rest_framework import routers
from .views import AuthorViewSet

router = routers.DefaultRouter()
router.register("", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),  # Including router.urls
]

app_name = "author"
