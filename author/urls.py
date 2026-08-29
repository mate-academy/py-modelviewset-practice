from django.urls import path, include
from author.views import AuthorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("author", AuthorViewSet, basename="manage")

app_name = "author"

urlpatterns = [
    path("", include(router.urls))
]
