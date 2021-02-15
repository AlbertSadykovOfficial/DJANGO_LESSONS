"""
 Написание контроллеров
    (Контроллеры, выполняющие 1 функцию)
        1 функция: Вывод, считываение и т.д
        ЕСЛИ нудно ВЫВЕСТИ на экран страницу для занесения нового обявления и ПОТОМ СОХРАНИТЬ данные в БД,
        ТО надо 2 контроллера такого рода.
"""
# Это должно быть написано в views.py
# 1я Контроллер-функция, котрая выводит на экран страницу добавления объявления
from django.shortcuts import render  # 2 вариант
from django.http import HttpResponse
from .forms import PosterForm


def add(request):
    pf = PosterForm()
    context = {'form': pf}
    return render(request, 'board/create.html', context)


# 2я Контроллер-функция, котрая сохранит объявления
def add_save(request):
    pf = PosterForm(request.POST)
    if pf.is_valid():
        pf.save()
        return HttpResponseRedirect(reverse('by_rubric',
                                            kwargs={'rubric_id': pf.cleaned_data['rubric'].pk}))
    else:
        context = {'form': pf}
        return render(request, 'board/create.html', context)


# После этого следует объявить к ним маршруты:
# from .views import add, add_save
# urlpatterns = [
#               path('add/save/', add_save, name='add')
#               path('add/', add, name='add')
#               ]
#
# Далее, в шаблоне board/create.html исправляем тег <form>:
#   <form action="{% url 'add_save' %}" method="post">
#

"""
 Контроллеры, выполняющие несколько задач одновременно

 (Выведет страницу с формой и выполнит созранение данных) 

"""


def add_and_save(request):
    if request.method == 'POST':
        pf = PosterForm(request.POST)
        if pf.is_valid():
            pf.save()
            return HttpResponseRedirect(reverse('by_rubric',
                                                kwargs={'rubric_id': pf.cleaned_data['rubric'].pk}))
        else:
            context = {'form': pf}
            return render(request, 'board/create.html', context)
    else:
        pf = PosterForm()
        context = {'form': pf}
        return render(request, 'board/create.html', context)

# После этого следует объявить к ним маршруты:
# from .views import add, add_save
# urlpatterns = [
#               path('add/save/', add_and_save, name='add')
#               ]
#
# Далее, в шаблоне board/create.html исправляем тег <form>
# Поскольку адрес создания объявления и занесения в БД один, то указывать адрес уже не нужно
#   <form method="post">
#
