from rest_framework.viewsets import ModelViewSet

from authors.models import Author, Biography
from authors.serializers import AuthorModelSerializer, BiographySerializer

class AuthorsViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer

