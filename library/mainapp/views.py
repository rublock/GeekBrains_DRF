from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer


from mainapp.models import Book, Article
from mainapp.serializers import BookSerializer, ArticleSerializer


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ArticlesViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@api_view(['GET'])
#@renderer_classes([JSONRenderer]) #API ввиде сырого JSON
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

