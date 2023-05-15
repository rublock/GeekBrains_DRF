from django.urls import path

import mainapp.views as mainapp


urlpatterns = [
    #path('article/list/api/view', mainapp.article_list),
    #тоже самое только Class based view
    path('article/list/api/view', mainapp.ArticleAPIView.as_view()),
]
