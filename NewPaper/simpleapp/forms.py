from .models import *
from django.forms import ModelForm, BooleanField


# Создаём модельную форму
class NewsForm(ModelForm):
    check_box = BooleanField(label='все верно')  # добавляем галочку, или же true-false поле

    class Meta:
        model = News
        fields = ['name', 'price', 'category', 'quantity', 'description', 'User', 'check_box']
