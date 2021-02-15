"""
    Классы, работающие с формами:

 Классы для работы с записями
    Классы из файла Form_Classes1.py - низкоуровневые, они не совсем удобны,
    они не предусматривают продолжительного хранения объекта формы,
    поэтому мы не может извлечь занесенные данные в нужный момент.
    При этом Перенос данных из формы в модель тоже приходится выплнять самостоятельно.
    Поэтому созданы более выоскоуровневые классы:

     Примесь ModelFormMixin:
        (Наследует SingleObjectMixin и FormMixin
         Аналогичен FormMixin, но нацелен на работу с формами, связанными с моделями)

         Атрибуты и методы (частично):
            model - создает ссылку на класс модели на основе который будет создана форма
            fields - последовательность имен полей модели, которые должны присутсвтвовать в форме
            get_form_class() - Возвращает ссылку на класс используемой формы (переопределен)
            form_valid(...) - обработка введенных в форму данных, в случае валидности (переопределен)
            success_url - хранит интернет адрес, на который будет выполнено перенаправление
                          ! В отличе от одноменного атрибута в FormMixin, он поддерживает указание
                            непосредственно в строке с интернет-адресом спец последовательностей
                            символов вида: {<имя поля таблицы в БД>}, вместо этого значения, классом
                            будет  подставлено значение поля с указыннм (именем)
                            НО должно подставляься имя (НЕ ПОЛЯ МОДЕЛИ),а имя (ТАБЛИЦЫ БД)
                            Т.е. (id), а НЕ(pk); (rubric_id),а НЕ(rubric):
                                success_url = '/board/detail/{id}'
                                success_url = '/board/{rubric_id}'


    Контроллер CreateView
        (Наследует View , ModelFormMixin, ProcessFormView, SingleObjectMixin,
                    SingleObjectTemplateResponseMixin, TemplateResponseMixin
        Обладает всей функциональностью по созданию, выводу, валидации форм,
                                           создания записи на основе занесенных в форму данных)

        Атрибуты:
            template_name_suffix - строка с суффиксом, который будет доавблен к сгенер шабл.(по умолчанию _form)
            object - хранит созданную в модели запись или None(если она не создана)

        Пример: class PosterCreateForm  (view.py)


    Контроллер UpdateView
        (Наследует от View, ModelFormMixin, ProcessFormView, SingleObjectMixin,
                    SingleObjectTemplateResponseMixin, TemplateResponseMixin
         Самостояельно находит в модели запись по полученным из URL-параметра ключу или слагу,
         выведет страницу с формой для правки, проверит и сохранит исправленные данные)

        Для поиска записи в модели, необходимо указать эту (model) и набор записей (queryset)
        или переопрделить get_queryset()

        Атрибуты:
            template_name_suffix - строка с суффиксом, который будет доавблен к сгенер шабл.(по умолчанию _form)
            object - хранит созданную в модели запись или None(если она не создана)


    Контроллер DeleteView
         (Наследует от View, ModelFormMixin, ProcessFormView, SingleObjectMixin,
                    SingleObjectTemplateResponseMixin, TemplateResponseMixin
          Самостояельно находит в модели запись по полученным из URL-параметра ключу или слагу,
          выведет форму с кнопкой, подтверждающую удаление)

        Атрибуты:
            template_name_suffix - строка с суффиксом, который будет доавблен к сгенерированному шаблону
                                   (по умолчанию _confirm_delete)
            object - хранит удаляемую в модели запись.
"""

# --------- Контроллер UpdateView
#
# Код для формы Редактирования записи
# + надо создать шаблон board\poster_form.html

# + Указать ссылки на изменения в index.html:
# <p><a href="{% url 'edit' pk=poster.pk %}">Изменить</a></p>

# + в файле urls.py прописать адрес
# path('edit/<int:pk>/', PosterEditView.as_view(), name='edit'),
from django.views.generic.edit import UpdateView
form .models import Poster, Rubric

class PosterEditView(UpdateView):
    model = Poster
    form_class = PosterForm
    success_url = '/board/' # Куда перенаправить, после изменений

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


# --------- Контроллер DeleteView
#
# Код для формы Редактирования записи
# + надо создать шаблон board\poster_confirm_delete.html

# + Указать ссылки на изменения в index.html:
# <p><a href="{% url 'delete_poster' pk=poster.pk %}">Изменить</a></p>

# + в файле urls.py прописать адрес
# path('delete_poster/<int:pk>/', PosterDeleteView.as_view(), name='delete_poster'),
from django.views.generic.edit import DeleteView
form .models import Poster, Rubric

class PosterDeleteView(DeleteView):
    model = Poster
    success_url = '/board/'

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context