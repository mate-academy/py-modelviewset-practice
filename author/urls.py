from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet


app_name = "author"  # Додай це!
router = DefaultRouter()
router.register(r"authors", AuthorViewSet, basename="manage")
urlpatterns = router.urls
