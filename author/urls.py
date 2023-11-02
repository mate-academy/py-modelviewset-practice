from rest_framework import routers

from author.views import AuthorViewSet


author_router = routers.DefaultRouter()
author_router.register("author", AuthorViewSet, basename="manage")

urlpatterns = [] + author_router.urls

app_name = "author"
