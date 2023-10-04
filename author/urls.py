# from django.urls import path, include
# from rest_framework import routers
#
#
# from author.views import AuthorViewSet
#
# router = routers.DefaultRouter()
# router.register("authors", AuthorViewSet, basename="author")
# # urlpatterns = [
# #     path("author/", include(router.urls)),
# # ]
# urlpatterns = router.urls
#
# app_name = "author"

#
# from rest_framework import routers
#
# from author.views import AuthorViewSet
#
# router = routers.SimpleRouter()
# router.register("authors", AuthorViewSet, basename="author")
# include((router.urls, 'app_name'), namespace='instance_name')),
# urlpatterns = router.urls
#
#
# app_name = "author"
from django.urls import include, path

from author.views import AuthorViewSet

# 1. імпортую роутери routers
from rest_framework import routers

# 2. Створюю роутер з routers.DefaultRouter()
router = routers.DefaultRouter()

# 3. У цей роутер реєструю потрібний набір ендпоінтів,
# який буде йти по ключовому слову "buses".
# Та вказую який ViewSet за це відповідатиме BusViewSet.
router.register("authors", AuthorViewSet)
# router.register("trips", TripViewSet)
urlpatterns = [
    path("", include((router.urls, "author"), namespace="author")),
]
#
# path('api/', include((router.urls, 'app_name'), namespace='instance_name')),
# 3. Вказую назву додатку.
app_name = "author"
