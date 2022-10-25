from django import forms
from .models import Article


class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'title', 'text']


class PostFormAddAuthor(PostForm):
    def save(self, commit=True):
        author = Article.objects.get_or_create(user=self.author)[0]
        self.instance.author = author
        return super().save(commit)
