from django.urls import path, include
from rest_framework import routers
from author.views import AuthorViewSet

app_name = "author"
router = routers.DefaultRouter()
router.register(
    r"manage",
    AuthorViewSet,
    basename="manage"
)

# Print the URL patterns to debug
for url_pattern in router.urls:
    print(url_pattern)

urlpatterns = [
    path("", include(router.urls)),
]
