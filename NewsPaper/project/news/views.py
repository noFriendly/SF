from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm, PostFormAddAuthor
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
class PostsList(ListView):
    model = Post
    ordering = ['-dateCreation']
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

class PostSearch(ListView):
    model = Post
    ordering = ['-dateCreation']
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostCreate(PermissionRequiredMixin, CreateView):
    form_class = PostFormAddAuthor
    model = Post
    template_name ='forms/create.html'
    permission_required = ('news.add_article',)

class PostDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'forms/delete.html'
    queryset = Post.objects.all()
    success_url = '/news/search'
    permission_required = ('news.delete_article',)

class PostUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'forms/update.html'
    model = Post
    form_class = PostForm
    permission_required = ('news.change_article',)
