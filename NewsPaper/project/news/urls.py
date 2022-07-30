from django.urls import path
from .views import PostsList, PostDetail, PostSearch, PostCreate, PostDelete, PostUpdate


urlpatterns = [
    path('', PostsList.as_view(),name='article_root'),
    path('<int:pk>', PostDetail.as_view(), name='article_detail'),
    path('search', PostSearch.as_view(), name='article_search'),
    path('add/', PostCreate.as_view(), name='article_create'),
    path('<int:pk>/delete', PostDelete.as_view(), name='article_delete'),
    path('<int:pk>/edit', PostUpdate.as_view(), name='article_update')
]