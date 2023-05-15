from django.urls import path

import mainapp.views as mainapp


urlpatterns = [
    #path('article/list/api/view', mainapp.article_list),
    #тоже самое только Class based view
    path('article/list/api/view', mainapp.ArticleAPIView.as_view()),
    path('article/create/api/view', mainapp.ArticleCreateAPIView.as_view()),
    #path('article/list/api/view', mainapp.ArticleListAPIView.as_view()),
    #path('article/retrieve/api/view/<int:pk>/', mainapp.ArticleRetrieveAPIView.as_view()),
    #path('article/delete/api/view/<int:pk>/', mainapp.ArticleDestroyAPIView.as_view()),
    path('article/update/api/view/<int:pk>/', mainapp.ArticleUpdateAPIView.as_view()),
]
