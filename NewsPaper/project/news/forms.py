from django import forms
from .models import Post, Author

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['categoryType', 'title', 'text', 'postCategory']

class PostFormAddAuthor(PostForm):

    def save(self, commit=True):
        author = Author.objects.get_or_create(user=self.authorUser)[0]
        self.instance.author = author
        return super().save(commit)
