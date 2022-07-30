from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post

class PostFilter(FilterSet):
    publication_date = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {'dateCreation', 'title', 'postCategory'}