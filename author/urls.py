from author.views import AuthorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("author", AuthorViewSet, basename="manage")
urlpatterns = router.urls

app_name = "author"
