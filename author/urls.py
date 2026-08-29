from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

app_name = "author"

router = DefaultRouter()
router.register(r"authors", AuthorViewSet, basename="authors")

custom_urlpatterns = [
    path(
        "authors/",
        AuthorViewSet.as_view({"get": "list", "post": "create"}),
        name="manage-list"
    ),
]

urlpatterns = custom_urlpatterns + router.urls
