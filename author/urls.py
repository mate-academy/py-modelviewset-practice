from author.views import AuthorViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("author", AuthorViewSet, basename="manage")

urlpatterns = router.urls

app_name = "author"
