from rest_framework import routers

from author.views import AuthorViewSet


router = routers.SimpleRouter()
router.register(r'authors', AuthorViewSet, basename="manage")

urlpatterns = router.urls
