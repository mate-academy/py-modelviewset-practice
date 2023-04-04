from django.urls import path, include
from rest_framework import routers

from author.views import AuthorViewSet

router_author = routers.DefaultRouter()
router_author.register("authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router_author.urls))
]

app_name = "author"
