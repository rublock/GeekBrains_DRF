from django.urls import path

import mainapp.views as mainapp


urlpatterns = [
    path('article/list/api/view', mainapp.article_list),
]
