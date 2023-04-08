from rest_framework import routers

from author.views import AuthorViewSet

route = routers.DefaultRouter()
route.register("authors", AuthorViewSet, basename="manage")

urlpatterns = route.urls

app_name = "author"
