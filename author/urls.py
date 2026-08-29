from django.urls import path, include
from rest_framework import routers

from author import views

router = routers.DefaultRouter()
router.register("author", views.AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls))
]


app_name = "author"
