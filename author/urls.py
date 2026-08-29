# Create your urls here
from django.urls import include, path
from rest_framework import routers

from .views import AuthorViewSet

router = routers.DefaultRouter()
router.register("authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls))

]


app_name = "author"
