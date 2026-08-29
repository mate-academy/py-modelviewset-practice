# Create your urls here
from unittest.mock import patch

from django.urls import include
from rest_framework import routers

from author.views import AuthorViewSet


app_name = "author"
router = routers.DefaultRouter()
router.register(r"author", AuthorViewSet, basename="manage")

urlpatterns = router.urls
