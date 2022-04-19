from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.db import models

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)


# импортировали класс формы, который предоставляет allauth

class BasicSignupForm(SignupForm):
    def save(self, request):
        # вызываем этот же метод класса-родителя (save), чтобы необходимые проверки и сохранение в модель User
        # были выполнены
        user = super(BasicSignupForm, self).save(request)
        # Важно!!! Переменная basic_group (ниже), аргумент name='basic' должен соответствовать названию группы в джанге
        basic_group = Group.objects.get(name='common')
        # через атрибут user_set, возвращающий список всех пользователей этой группы, мы добавляем нового
        # пользователя в эту группу
        basic_group.user_set.add(user)
        # Обязательным требованием метода save() является возвращение объекта модели User по итогу выполнения функции
        return user
# Create your models here.
