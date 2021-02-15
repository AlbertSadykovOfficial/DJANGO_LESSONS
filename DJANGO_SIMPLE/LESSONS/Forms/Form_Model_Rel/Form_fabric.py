"""

    Создание форм связанных с моделью посредством фабрики классов

        modelform_factory(<модель>[, fields=None][, exclude=None]
                                   [, labels=None][, help_texts=None]
                                   [, error_message=None][, field_classes=None]
                                   [, widgets=None][, form=<форма, связанныая с моделью>])
            <модель> - ссылка на модель
            fields   - последовательность имен полей модели, которые должны быть включены в создаваемую форму.
                       __all__ - использовать все модели
            exclude - поля, которые не лолжны влючаться в форму
            labels - надписи для полей формы
            help_texts - поясняющий текст для полей формы
            error_message - строковое сообщение об ошибках (словарь, ключ=> поля)
            field_classes - указывает поле какого типа должно быть создано в форме
            widgets - задает элемент управления
            form - указание формы, связанной с моделью

        Функция вернет готовый класс формы

    Фабрики классов удобно использовать в контроллер-функциях для создания редко используемых форм.
    В этом случае класс не занимает место в Оперативной памяти, т.к создается только при необходимости
    и удаляется как только перестает существовать хранящая его переменная

"""

# Форма с применением фабрики классов:
#
# Класс, сохраненный в PosterForm, модно использовать как и раньше
# class PosterCreateForm(CreateView):
#      form_classes = PosterForm

from django.forms import modelform_factory, DecimalField
from django.forms.widgets import Select

from .models import Poster, Rubric

PosterForm = modelform_factory(Poster,
                               fields=('title', 'content', 'price', 'rubric'),
                               labels={'title': 'Название товара'},
                               help_texts={'rubric': 'Не забудьте выбрать рубрику'},
                               field_classes={'price': DecimalField},
                               widgets={'rubric': Select(attrs={'size': 8})}
                               )