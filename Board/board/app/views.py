from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Article
from .filters import PostFilter
from .forms import PostForm, PostFormAddAuthor
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.
class ArticleList(ListView):
    model = Article
    context_object_name = 'article_list'
    queryset = Article.objects.order_by('-dateCreation')
    paginate_by = 15


class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article_detail'


class ArticleSearch(ListView):
    model = Article
    ordering = ['-dateCreation']
    template_name = 'search.html'
    context_object_name = 'article_list'
    paginate_by = 15

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticleCreate(PermissionRequiredMixin, CreateView):
    form_class = PostFormAddAuthor
    model = Article
    template_name = 'forms/create.html'
    permission_required = ('news.add_article',)


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'forms/delete.html'
    queryset = Article.objects.all()
    success_url = '/news/search'
    permission_required = ('news.delete_article',)


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'forms/update.html'
    model = Article
    form_class = PostForm
    permission_required = ('news.change_article',)
