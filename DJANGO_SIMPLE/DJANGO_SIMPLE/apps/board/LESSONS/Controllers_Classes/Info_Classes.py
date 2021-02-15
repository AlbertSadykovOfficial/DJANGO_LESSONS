"""
    Классы-выводящие сведения о выбранной записи (django.views.generic.detail)
    (Добавление возможности просмтора сведений о выбранном объявлении (цены на товар...))

    Классы являются более высокоуровневыми (обобщенными), чем Базовые, посколько выполняюттиповые задачи

 Примесь SingleObjectMixin:
    (Извлекает запись из модели по ключу (или сленгу), которые он сам получает из URL-параметров,
    затем помещает запись в контекст Шаблона)

    Поддерживает множество аттрибутов и методов, часть из них:
        model - задает модель для извлечения записи
        queryset - набор записей в которых будет вестись поиск записи (QuerySet)
        get_queryset() - возвращает набор записй (QuerySet)
        ...
        context_object_name - имя переменной контекста шаблона
        get_object(...) - поиск записи по указанным критериям
        get_context_data(...) - переопределенный метод, создающий и возвращающий контекст данных

 Примесь SingleObjectTemplateResponseMixin
    (Рендеринг шаблона на основе найденной в модели записи)

    Атрибуты:
        template_name_field - путь к шаблону
        template_name_suffix- строка с суффиксом, который будет добавлен к авт. сгенер. пути к шаблону
                              (по умлочанию: '_detail')
    Методы:
        get_template_names() - переопределенный метод, возвращающий список путей к шаблонам в виде строк

 Контроллер DetailView(ВСЁ ВМЕСТЕ)^
    (Наследует View, TemplateResponseMixin, SingleObjectMixin, SingleObjectTemplateResponseMixin,
     самостоятельно ищет запись по значению ключа или слага, заносит в атрибут object, выводит страницу со сведениями)

"""
#
# from .views import PosterDetailView
# Добавтиь в urlpatterns:
# path('detail/<int:pk>/', PosterDetailView.as_view(), name='detail')
#
# + Создать шаблон board/poster_detail.html
#
# Добавить в шаблоны (index и by_rubric)сслыки:
# <h2><a href="{% url 'detail' pk=poster.pk %}">{{ poster.title}}</a></h2>

from django.views.generic.detail import DetailView
from .models import Poster, Rubric

class PosterDetailView(DetailView):
    model = Poster

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context