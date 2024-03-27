from django.urls import include, path
from rest_framework import routers

from author import views

router = routers.DefaultRouter()
router.register("authors", views.AuthorViewSet, basename="manage")

app_name = "author"
urlpatterns = [
    path("", include(router.urls))
]
