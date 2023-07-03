from rest_framework import routers

from author.views import AuthorViewSet

router = routers.DefaultRouter()
router.register("manage-list", AuthorViewSet)

urlpatterns = [

] + router.urls

app_name = "author"
