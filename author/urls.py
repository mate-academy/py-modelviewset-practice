from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AuthorViewSet

app_name = "author"

router = SimpleRouter()
router.register(r"authors", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]
