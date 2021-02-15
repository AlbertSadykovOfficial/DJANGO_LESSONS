"""

    Базовые Контроллеры-классы (django.views.generic.base)

 Контроллер View:
    (Оперделяет HTTP метод, посредством которого был выполнен запрос)

    Атрибуты:
        http_method_names  - Список имен допустимых методов
    Методы:
        dispatch(...) - Извлекает метод,вызывает,возвращает ответ, представленный экземпляром класса HttpResponse
        http_method_not_allowed(...) - Вызывается, если запрос выполнен с неподдерживаемого Http-метода
        options(...) - Обрабатывает запро с применением Http-Метода OPTIONS

    В процессе работы класс создает несколько атрибутов:
        request - запрос, представленный экз.кл Request
        kwargs  - словарь с полученными из адресов URL-парамтрами


 Примесь ContextMixin
    (Добавляет контроллеру-классу средства для формирования контекста шаблона)

    extra_context - атрибут, задающий содержимое контекста шаблона
    get_context_data(...)- создает и возвращает контекст данных

 Примесь TemplateResponseMixin
    (Добавляет средства рендеринга Шаблона)

    Атрибуты:
        template_name - атрибут, задающий путь к шаблоу в виде строки
        content_type  - MIME-тип
    Методы:
        get_template_name() - список путей к шаблонам,заданных в виде строк
        render_to_response(...)- выполняет рендеринг шаблона и возвращает TemplateResponse

 Контроллер TemplateView (ВСЁ ВМЕСТЕ)
    (Наследует View, ContextMixin, TemplateResponseMixin,
     Автоматически выполняет рендеринг шаблона и отправляет ответ при получении запроса по методу GET)

"""

# Вывод главной страницы сайта с объявлениями (альтернатива index() во view.py)
from django.views.generic.base import TemplateView
from .models import Poster, Rubric

class PosterIndexView(TemplateView):
    template_name = 'board/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['posters_pull']  = Poster.objects.all()
        context['rubrics']       = Rubric.objects.all()
        return context