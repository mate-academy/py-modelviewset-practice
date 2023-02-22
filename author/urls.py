from author.views import AuthorViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register("authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "author"
