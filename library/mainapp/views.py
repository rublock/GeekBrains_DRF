from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView




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

#тоже самое только Class based view
class ArticleAPIView(APIView):
	renderer_classes = [JSONRenderer] #API ввиде сырого JSON
	
	def get(self, request, format=None):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)

from rest_framework.views import APIView

class ArticleCreateAPIView(CreateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
        
class ArticleListAPIView(ListAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class ArticleRetrieveAPIView(RetrieveAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	
class ArticleDestroyAPIView(DestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	
class ArticleUpdateAPIView(UpdateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer





