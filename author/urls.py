from django.urls import include, path
from author.views import AuthorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("author", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]
app_name = "author"
