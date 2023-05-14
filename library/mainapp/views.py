from rest_framework.viewsets import ModelViewSet


from mainapp.models import Book, Article
from mainapp.serializers import BookSerializer, ArticleSerializer


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ArticlesViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
