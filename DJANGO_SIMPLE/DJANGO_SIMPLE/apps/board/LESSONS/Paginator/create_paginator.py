"""
    Создание пагинатора

    Класс Paginator модуль (django.core.paginator)

    Конструкор:
        Paginator(<набор записей>, <кол-во записей в части>[, orphans=0][, allow_empty_first_page=True])
                <набор записей> - Что должно разбиваться на части
                orphans - минимальное кол-во записей, что могут пристутствовать в последней чати пагинатора
                          Если в последней части меньш записей, она будет выведена с предыдущей,
                          Если задать 0 - в последней части моде присутствовать сколько угодно частей
                allow_empty_first_page- создавать ли пустую часть ,если набор не содержит записей

        Атрибуты:
            count - общее кол-во записей во все частях
            num_pages- кол-во частей, на которые будет разбит весь набор
            page_range- итератор, последовательно возвращаюй номера всех частей пагинатора (начинается с 1).

        Однако для нас полезнее будут два метода этого класса:
            get_page(<номер части>) - вернет экземпляр класса Page, представляющий часть с указанным номером
                                       Если в номер указано не число - вернется 1 страница
                                       Если в номер указано не целое число, возбуждается исключение
            page(<номер части>) - то же, что и get_page
"""

# Главная страница (index) с использованием пагинатора
# Выводит список объявлений разбитых на части, номер части передается через параметр GET page

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Poster, Rubric

def index(request):
    rubrics = Rubric.objects.all()
    posters_pull = Poster.objects.all()
    paginator = Paginator(posters_pull, 2)
    # Если параметр страницы присутствует, мы извлекаем из него номер части, иначе отдаем 1ю страницу
    if 'page' in request.GET:
        page_num  =request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'rubrics': rubrics, 'page': page, 'posters_pull': page.object_list}
    return render(request, 'board/index.html', context)