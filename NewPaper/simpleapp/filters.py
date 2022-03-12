from django_filters import FilterSet, DateTimeFromToRangeFilter
from .models import News
from django import template
from django_filters.widgets import RangeWidget


register = template.Library()

# создаём фильтр
class NewsFilter(FilterSet):
     class Meta:
        model = News
        fields = ('name', 'price', 'quantity', 'category') # поля, которые мы будем фильтровать


class SearchFilter(FilterSet):
    date_pub = DateTimeFromToRangeFilter(lookup_expr=('icontains'), widget=RangeWidget(attrs={'type': 'datetime-local'}))

    class Meta:
        model = News
        fields = ('date_pub', 'User')





