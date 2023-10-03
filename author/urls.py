# 2. full GenericViewSet & Mixins with routers(better).
# Можна додавати більше ендпоінтів у перспективі.
# from django.urls import include, path
#
# from .views import AuthorViewSet
#
# # 1. імпортую роутери routers
# from rest_framework import routers
#
# # 2. Створюю роутер з routers.DefaultRouter()
# router = routers.DefaultRouter()
#
# # 3. У цей роутер реєструю потрібний набір ендпоінтів,
# # який буде йти по ключовому слову "buses".
# # Та вказую який ViewSet за це відповідатиме BusViewSet.
# router.register("authors", AuthorViewSet)
# # router.register("trips", TripViewSet)
# urlpatterns = [
#     path("", include(router.urls))
# ]
#
# # 3. Вказую назву додатку.
# app_name = "author"

# #1. full GenericViewSet & Mixins with routers
# from django.urls import path
#
# from .views import AuthorViewSet
#
# # 1. імпортую роутери routers
# from rest_framework import routers
#
# # 2. Створюю роутер з routers.DefaultRouter()
# router = routers.DefaultRouter()
#
# # 3. У цей роутер реєструю потрібний набір ендпоінтів,
# # який буде йти по ключовому слову "buses".
# # Та вказую який ViewSet за це відповідатиме BusViewSet.
# router.register("author", AuthorViewSet)
#
# urlpatterns = router.urls
#
# # 3. Вказую назву додатку.
# app_name = "author"


# full GenericViewSet & Mixins
# використовується рідко такий запис. Частіше використовують роутери.
from django.urls import path

from .views import AuthorViewSet


author_list = AuthorViewSet.as_view(actions={
    "get": "list",
    "post": "create",
})

author_detail = AuthorViewSet.as_view(actions={
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    path("authors/", author_list, name="author-list"),
    path("authors/<pk>/", author_detail, name="author-detailed"),
    # endpoint, view, name
]


# # 3. Вказую назву додатку.
app_name = "author"
