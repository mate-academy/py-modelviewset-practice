from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

app_name = "author"

router = DefaultRouter()
router.register("authors", AuthorViewSet, basename="manage")

urlpatterns = router.urls
