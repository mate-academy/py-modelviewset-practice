from django.urls import path, include
from rest_framework.routers import SimpleRouter

from author.views import AuthorViewSet

router = SimpleRouter()
router.register(r"authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "author"
