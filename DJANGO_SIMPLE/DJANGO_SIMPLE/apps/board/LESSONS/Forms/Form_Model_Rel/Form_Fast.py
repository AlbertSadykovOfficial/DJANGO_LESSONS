"""

    Создание форм путем быстрого объявления

        Если форма, связанная с моделью нуна на проолжительное время,
        имеет смысл прибегнуть ко 2 способу:
        Объявить класс формы вручную

        Такой класс должен быть производным от ModelForm
        В этом классе объявляется вложенный класс Met, в котором записывается набор атрибутов класса,
        имеющих те же имена, что и параметры функции modelform_factory()

"""

from django.forms import ModelForm, DecimalField
from django.forms.widgets import Select
from .models import Poster

class PosterForm(ModelForm):
    class Meta:
        model = Poster
        fields = {'title', 'content', 'price', 'rubric'}
        labels = {'title': 'Название товара'}
        help_texts = {'rubric': 'Не забудьте задать рубрику'}
        field_classes = {'price': DecimalField}
        widgets = {'rubric': Select(attrs={'size': 8})}

