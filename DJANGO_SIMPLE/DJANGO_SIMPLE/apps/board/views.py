# ФАЙЛ исполнений
from django.http import HttpResponse
from django.template import loader # 1 вариант
from django.shortcuts import render # 2 вариант

from .models import Poster, Rubric

from django.views.generic.dates import ArchiveIndexView
# PosterCreateForm
from django.views.generic.edit import CreateView
from .forms import PosterForm
from django.urls import reverse_lazy

# PosterEditView
from django.views.generic.edit import UpdateView

# PosterDeleteView
from django.views.generic.edit import DeleteView

# PosterByRubricView
from django.views.generic.list import ListView

# PosterCreateView
from django.views.generic.detail import DetailView

from django.core.paginator import Paginator
def index(request):
    rubrics = Rubric.objects.all()
    posters_pull = Poster.objects.all()
    paginator = Paginator(posters_pull, 2)
    # Если параметр страницы присутствует, мы извлекаем из него номер части, иначе отдаем 1ю страницу
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'rubrics': rubrics, 'page': page, 'posters_pull': page.object_list}
    return render(request, 'board/index.html', context)

# Главная страница процедурный метод
def index1(request):
    # Не работает <a href="{% url 'by_rubric' rubric.pk %}"> {{ rubric.name }}</a>
    posters_pull = Poster.objects.all()
    rubrics      = Rubric.objects.all()
    context = {'posters_pull': posters_pull, 'rubrics': rubrics}
    return render(request, 'board/index.html', context)

# Главная страница ООП метод
class PosterIndexView(ArchiveIndexView):
    model = Poster
    date_field = 'published'
    template_name = 'board/index.html'
    context_object_name = 'posters_pull'
    allow_empty = True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

from django.forms import modelformset_factory
def folder(request):
    return HttpResponse('Im in Folder')

# 1 вариант работы с шаблонами (шаблоны должны располагаться в папке templates -> <app_name> -> temp.html)
def html_temp1(request):
    template = loader.get_template('board/index1.html')
    # Надо иметь записи в БД
    posters_pull = Poster.objects.order_by('-published')
    context = {'posters_pull': posters_pull}
    return HttpResponse(template.render(context, request))

# 2 вариант работы с шаблонами (шаблоны должны располагаться в папке templates -> <app_name> -> temp.html)
def html_temp2(request):
    posters_pull = Poster.objects.order_by('-published')
    return render(request, 'board/index1.html', {'posters_pull': posters_pull})

# rubric_id будет присвоено значение URL параметра
# Сортировка по ключу, всем рубрикам и текущей рубрики(чтобы вывожить ее название)
def by_rubric(request, rubric_id):
    posters_pull    = Poster.objects.filter(rubric=rubric_id)
    rubrics         = Rubric.objects.all()
    current_rubric  = Rubric.objects.get(pk=rubric_id)
    context = {'posters_pull': posters_pull, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'board/by_rubric.html', context)

# Объектаная реализация функции by_rubric
class PosterByRubricView(ListView):
    template_name = 'board/by_rubric.html'
    context_object_name = 'posters_pull'

    def get_queryset(self):
        return Poster.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context


# Класс CreateView включает функциональность создания формы и вывода ее на экран, получение данных, проверке на коррктность
class PosterCreateForm(CreateView):
    template_name = 'board/create.html' # Путь к файлу Шаблона, который будет использован для вывода страницы
    form_class    = PosterForm          # Класс формы, связанный с моделью
    #success_url   = '/hello/'           # Адрес на который удет перенаправение после успешного сохранения данных
    success_url = reverse_lazy('index')

    # Переопределим метод, чтобы добавить в контекст дополнительные данные - список рубрик
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

# Код для Редактирования объявлений
class PosterEditView(UpdateView):
    model = Poster
    form_class = PosterForm
    success_url = '/board/' # Перенаправляем на главную после внесения изменений

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

# Код для Удаления объявлений
class PosterDeleteView(DeleteView):
    model = Poster
    success_url = '/board/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class PosterDetailView(DetailView):
    model = Poster

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context