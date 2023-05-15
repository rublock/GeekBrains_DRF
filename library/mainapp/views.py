from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, get_object_or_404




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

#если нужно построить свою логику
class ArticleViewSet(ViewSet):
	def list(self, request):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)
	
	def retrieve(self, request, pk=None):
		article = get_object_or_404(Article, pk=pk)
		serializer = ArticleSerializer(article)
		return Response(serializer.data)
	
	#если нужно вывести только одно поле данных
	@action(detail=True, methods=['get'])
	def article_text_only(self, request, pk=None):
		article = get_object_or_404(Article, pk=pk)
		return  Response({'article.text': article.text})
