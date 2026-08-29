from django.urls import path, include
from author.views import AuthorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("manage", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls), name="author"),
]

app_name = "author"
