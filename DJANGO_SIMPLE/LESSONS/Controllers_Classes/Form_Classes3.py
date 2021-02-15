"""
    Классы для вывода хронолигческих списков (django.views.generic.dates)
    (за год, месяц, неделю, текущее число или дату)

 Вывод самых новых записей

    Примесь DateMixin
        (фильтрация записей по дате)

        Атрибуты:
            date_field - имя поля модули типа DateField или DateTimeField
            get_date_field() - возвращает имя поля модели со значениями даты
            allow_future - True: Велючить в набор записей поля, больше текущего ("будущие" записи)
            get_allow_future()

    Контроллер BaseDateListView
        (Наследует от DateMix, MultipleObjectMixin
         База для более специаллизированных классов;
         Задает сортировку по убыванию значения поля, возвращенного методом get_date_field())

         Атрибуты:
            allow_empty - True:разрешает извлечене пустой записи
            date_list_period - Атрибут, показывающий по какой части следует урезать значение даты
            get_date_items() - вернет кортеж их 3х элементов:
                                - список дат, для которых в наборе существуют хаписи
                                - набор записей
                                - словарь, элементы которого будут добавлены в контекст шаблона
            get_dated_queryset(...)- вернет набор записей, отфильтрованный по заданным условиям
            ...

         Класс добавляет в контекст шаблона 2 доп жлемента:
            object_list - результирующий набор записей
            date_list - список урезанных значений дат, для которых в наборе есть записи


    Контроллер ArchiveIndexView
        (Наследует от View, DateMixin, BaseDateListView, TemplateResponseMixin,
                      MultipleObjectMixin, MultipleObjectTemplateResponseMixin
         Выводит хронолигический список записей, отсортированных по убыванию значения заданного поля)

         Для хранения результирующего набора выводимых записей в контексте шаблона создается переменная latest/
         В переменных date_list контекста шаблона хранится список значений дат, урезанных до года.
         К автоматически сгенерироанному пути к шаблону по умолчанию добавляется суффикс _archive


    Вывод записей по <периоду> = { годам(Year), месяцам(Month), неделям(Week), дням(Day) }:
        Примесь <период>Mixin
        Контроллер <период>ArchiveMixin

"""

# Главная страница через Объект
from django.views.generic.dates import ArchiveIndexView
from .models import Poster, Rubric

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