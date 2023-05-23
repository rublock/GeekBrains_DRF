from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from authors.views import AuthorsViewSet, BiographyViewSet
from mainapp.views import BooksViewSet, ArticlesViewSet

router = DefaultRouter()
router.register('authors', AuthorsViewSet)
router.register('biography', BiographyViewSet)
router.register('books', BooksViewSet)
router.register('articles', ArticlesViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('views/', include('mainapp.urls')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
]
