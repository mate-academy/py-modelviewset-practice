from django.urls import path

from author.views import AuthorListCreateView, AuthorRetrieveUpdateDestroyView


urlpatterns = [
    path("authors/", AuthorListCreateView.as_view(), name="manage-list"),
    path(
        "authors/<int:pk>/",
        AuthorRetrieveUpdateDestroyView.as_view(),
        name="manage-detail"
    ),
]

app_name = "author"
