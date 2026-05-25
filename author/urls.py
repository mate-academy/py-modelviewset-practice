# Create your urls here
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from author.views import AuthorViewSet

app_name = "author"

router = DefaultRouter()
router.register("manage", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]
