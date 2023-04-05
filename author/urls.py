from author.views import AuthorViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register("author", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "author"
