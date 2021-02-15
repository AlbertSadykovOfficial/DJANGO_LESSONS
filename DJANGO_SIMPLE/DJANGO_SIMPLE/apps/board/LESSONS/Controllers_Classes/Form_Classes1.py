"""
    Классы, работающие с формами:

 Классы вывода и валидации форм:
    Примесь FormMixin
        (Производный от класса ContextMixin
         Создание формы, проверка введенных данных, выплнить перенаправление, если данные введены верно
         или выполнить повторный вывод формы в противном случае)

         Атрибуты:
            form_class - хранит ссылку на класс формы
            initial    - хранит словарь с изначальными данными для занесения в созданную форму.
            success_url- хранит адресс на который будет выполнено перенаправление
            ...
         Методы:
            get_form_class() - вернет сслыку на класс используемой формы
            get_context_data(...) - переопределенный метод, создающий и возвращающий контекст данных
            form_valid(...) - Обработка данных в случае прохождения валидации
            form_invalid(...) - Выполняет обработку ситуации, когда введенные в форму данные не проходят валидацию
            ...

    Контроллер ProcessFormView:
        (Производный от класса View
         Выводит форму на экран, принимает введенные данные и проводит вальдацию)

         Переопределяет 3 метода базового класса:
            get(...)  - выводит форму на экран
            post(...) - получает введенные в форму данные  выполняет их валидацию.
                        Если валидация успешна, вызывает: form_valid(), иначе form_invalid()
            put(...)  - То же, тчо и post

    Контроллер FormVeiw:
        (Производный от View, FormMixin, ProcessFormView, TemplateResponseMixin
         Преставляет все инструменты для обработки форм (создать, вывести по шаблону, проверка корректности))

"""

# FormVeiw - (Добавление на доску нового объявления)

from django.views.generic.edit import FormView
from django.urls import reverse
from .models import Poster, Rubric

class PosterAddView(FormView):
    template_name = 'board/create.html'
    form_class = PosterForm
    initial = {'price': 0.0}

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
    # Сохранение введенных данных
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    # Запоминаем созданную форму в атрибуте object,
    # чтобы получить значение ключа рубрики объявления
    # Чтобы после сохранения объявления сформировать интрернет-адрес для перенаправления
    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object
    # Плучаем доступ к форме с занесенными данными
    def get_success_url(self):
            return reverse('board:by_rubric',
                           kwargs={'rubric_id': self.object.cleaned_data['rubric'].pk})