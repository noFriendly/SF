from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import UserResponse


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
        model = UserResponse
        fields = {'dateCreation', 'article'}
