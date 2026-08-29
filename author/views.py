# from rest_framework import generics
from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer

# class AuthorListCreateView(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
