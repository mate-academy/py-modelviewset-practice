from django.urls import include, path
from rest_framework import routers
from author.views import AuthorViewSet  # або твоя назва в'юсету

app_name = "author"

router = routers.DefaultRouter()
# ОБОВ'ЯЗКОВО вкажи basename="manage", щоб з'явився шлях "manage-list"
router.register("manage", AuthorViewSet, basename="manage")

urlpatterns = [
    path("", include(router.urls)),
]
