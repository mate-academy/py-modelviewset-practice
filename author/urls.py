from django.urls import include, path
from rest_framework import routers

from author.views import AuthorViewSet

router = routers.SimpleRouter()
router.register("authors", AuthorViewSet, basename="manage")

urlpatterns = router.urls

app_name = "author"
