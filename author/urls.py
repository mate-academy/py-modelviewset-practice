from django.urls import path, include
from rest_framework import routers
from author.views import AuthorViewSet

router = routers.DefaultRouter()
# Додаємо basename='manage', щоб створилися імена manage-list та manage-detail
router.register(r"author", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "author"
