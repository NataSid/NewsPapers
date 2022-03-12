from django.urls import path

from .views import *

urlpatterns = [
    path('', NewsList.as_view()),
    path('Search/', SearchList.as_view()),
    path('<int:pk>', PeperDetail.as_view(), name='Detail'), #ссылка на детали заказа
    path('Add/', AddList.as_view(), name='Add'), #ссылка на добавление товара
    path('Create/<int:pk>', NewsUpdateView.as_view(), name='Update'), #ссылка на редактирование
    path('Delete/<int:pk>', NewsDeleteView.as_view(), name='Delete'), #ссылка на удаление

]
