from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

app_name = "author"

router = DefaultRouter()

router.register(r"authors", AuthorViewSet, basename="author")

urlpatterns = router.urls
