from django.urls import path, include
from author.views import AuthorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
app_name = "author"

router.register("author", AuthorViewSet, basename="manage")

urlpatterns = [path("", include(router.urls))]
