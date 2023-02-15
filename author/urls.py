# Create your urls here
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from author.views import AuthorViewSet

router = routers.DefaultRouter()
router.register("manage-list", AuthorViewSet, basename="manage")
urlpatterns = [
    path("", include(router.urls))
]
urlpatterns += router.urls

app_name = "author"
