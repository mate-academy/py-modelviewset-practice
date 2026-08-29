from django.urls import path

from author.views import AuthorList, AuthorDetail

urlpatterns = [
    path("authors/", AuthorList.as_view(), name="manage-list"),
    path("authors/<int:pk>/", AuthorDetail.as_view(), name="manage-detail"),
]

app_name = "author"
