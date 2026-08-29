from django.urls import path, include
from rest_framework import routers

from author.views import AuthorViewSet

app_name = "author"

router = routers.DefaultRouter()
router.register("authors", AuthorViewSet)
urlpatterns = [path("", include(router.urls))]
