from django.urls import include, path
from rest_framework import routers
from author.views import AuthorViewSet

router = routers.DefaultRouter()
router.register("manage", AuthorViewSet, basename="manage")

app_name = "author"


urlpatterns = [
    path("", include(router.urls)),
]
