from django.urls import path
from .views import AuthorListCreateView, AuthorRetrieveUpdateDestroyView

app_name = "author"

urlpatterns = [
    path(
        "authors/",
        AuthorListCreateView.as_view(),
        name="manage-list"
    ),
    path(
        "authors/<int:pk>/",
        AuthorRetrieveUpdateDestroyView.as_view(),
        name="author-detail"
    ),
]
