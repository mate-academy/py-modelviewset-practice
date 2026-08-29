from rest_framework import routers
from django.urls import include, path

from author.views import AuthorViewSet

router = routers.DefaultRouter()
router.register("author", AuthorViewSet, basename="manage")

urlpatterns = router.urls

app_name = "author"
