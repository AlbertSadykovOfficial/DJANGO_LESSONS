"""
    Классы, выводящий наборы записей


 Примесь MultiplyObjectMixin:
    (Извлечение наборов записи из моделей
                с возможностью фильтрации, сортировки и разбиения
                полученные записи помещает в контекст шаблона)

    Номер, который нужно извелчь передается в составе интернет адреса чреез URL или GET-параметр page.
    Номер должен быть целочисленным и должен начинаться с 1.

    Атрибутов и методов много, часть из них:
        model - модель извлечения записи
        ordering - параметры сортировки (строки с именами полей)
        get_ordering() - возвращает параметры сортироки
        ...
        page_kwarg - атрибу, укзаывающий имя URL или GET ПАРАМЕТР, через корторый будет передаваться №
        allow_empty- True:разрешает извлечение "пустой" части. False: будет возбуждено исключение Http404
        paginator_class - класс используемого пагинатора. По умолчанию Paginator (django.core.paginator)
        ...
        context_object_name - имя переменной контекста шаблона
        ...


 Примесь MultiplyObjectTemplateResponseMixin:
    (Наседутеся от TemplateResponseMixin
     Выполняет рендерингшаблона на основе извлеченного набора записей object_list)

     Атрибут:
        template_name_suffix - строка с суффиксом, который будет добавлен к авт. сгенер. пути к шаблону
                              (по умлочанию: '_list')
     Методы:
        get_template_names() - переопределенный метод, возвращающий список путей к шаблонам в виде строк


 Контроллер ListView(ВСЁ ВМЕСТЕ)
    (Наследует View, TemplateResponseMixin, MultiplyObjectMixin, MultiplyObjectTemplateResponseMixin,
     самостоятельно извлекает из модели набор записей, заносит в атрибут object_list, выводит страницу со сведен

"""
# Альтернатива функции by_rubric (view.py)
from django.views.generic.list import ListView
from .models import Poster, Rubric

class PosterByRubricView(ListView):
    template_name = 'board/by_rubric.html'
    context_object_name = 'poster'

    def get_queryset(self):
        return Poster.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context