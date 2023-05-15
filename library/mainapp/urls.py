from django.urls import path, include
from rest_framework.routers import DefaultRouter

import mainapp.views as mainapp

mainapp_router = DefaultRouter()
mainapp_router.register('article', mainapp.ArticleViewSet, basename='article')
# mainapp_router.register('filter', mainapp.ArticleQuerySetFilterViewSet)


urlpatterns = [
    path('view/set/', include(mainapp_router.urls)),
    #path('article/list/api/view', mainapp.article_list),
    #тоже самое только Class based view
    path('article/<str:name>/', mainapp.ArticleKwargsFilterViewSet.as_view()),
    path('article/list/api/view', mainapp.ArticleAPIView.as_view()),
    path('article/create/api/view', mainapp.ArticleCreateAPIView.as_view()),
    #path('article/list/api/view', mainapp.ArticleListAPIView.as_view()),
    #path('article/retrieve/api/view/<int:pk>/', mainapp.ArticleRetrieveAPIView.as_view()),
    #path('article/delete/api/view/<int:pk>/', mainapp.ArticleDestroyAPIView.as_view()),
    path('article/update/api/view/<int:pk>/', mainapp.ArticleUpdateAPIView.as_view()),
]
