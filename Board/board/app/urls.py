from django.urls import path
from .views import ArticleList, ArticleDetail, ArticleCreate, ArticleDelete, ArticleUpdate, ArticleSearch

urlpatterns = [
    path('', ArticleList.as_view()),
    path('<int:pk>', ArticleDetail.as_view()),
    path('add/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),
    path('<int:pk>/edit', ArticleUpdate.as_view(), name='article_update'),
    path('search/', ArticleSearch.as_view(), name='article_search'),
]
