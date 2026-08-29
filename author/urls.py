# from django.urls import path
# from author import views
from rest_framework.routers import DefaultRouter
from author.views import AuthorViewSet

# from .views import AuthorListCreateView,
# AuthorRetrieveUpdateDestroyView

# urlpatterns = [
#     path('manage-list',
# AuthorListCreateView.as_view(), name='manage-list'),
#     path('manage-list/<int:pk>/',
# AuthorRetrieveUpdateDestroyView.as_view(), name='manage-detail'),
# ]

app_name = "author"

router = DefaultRouter()
router.register("authors", AuthorViewSet, basename="manage")

urlpatterns = router.urls

# urlpatterns = [
#     path('manage-list',
# 'author.views.AuthorListCreateView', name='manage-list'),
#     path('manage-list/<int:pk>/',
# 'author.views.AuthorRetrieveUpdateDestroyView', name='manage-detail'),
# ]


# urlpatterns = [
#     path('manage-list',
# views.AuthorListCreateView.as_view(), name='manage-list'),
#     path('manage-list/<int:pk>/',
# views.AuthorRetrieveUpdateDestroyView.as_view(), name='manage-detail'),
# ]
