from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .filters import NewsFilter, SearchFilter
from .models import *
from .forms import NewsForm



class NewsList(ListView):
    model = News
    template_name = 'flatpages/News.html'   #гланая общая страница
    context_object_name = 'News' #все объекты
    queryset = News.objects.order_by('-date_pub')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context



class PeperDetail(DetailView):
    model = News
    template_name = 'flatpages/Peper.html'   #детальная инфа
    context_object_name = 'Peper'
    queryset = News.objects.all()


class SearchList(ListView):
    model = News
    template_name = 'flatpages/Search.html'
    context_object_name = 'Search'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SearchFilter(self.request.GET, queryset=self.get_queryset())
        return context



class AddList(CreateView):
    model = News
    template_name = 'flatpages/Add.html'  #добавление
    form_class = NewsForm
    success_url = '/News/'



class NewsUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'flatpages/Create.html' #редактирование
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return News.objects.get(pk=id)


class NewsDeleteView(DeleteView):
    template_name = 'flatpages/Delete.html'   #удаление
    context_object_name = 'News'
    queryset = News.objects.all()
    success_url = '/News/'


class DeleteNews(PermissionRequiredMixin, NewsDeleteView):
    permission_required = ('NewPaper.delete_News',)

class AddNews(PermissionRequiredMixin, AddList):
        permission_required = ('NewPaper.Add_News',)

class UpdateNews(PermissionRequiredMixin, NewsUpdateView):
        permission_required = ('NewPaper.Update_News',)