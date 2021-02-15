"""

     Создание форм путем полного объявления

        Метод фабрикации и быстрый метод создания форм имеют недостаток:
        они позволяют задать для полей формы весьма ограниченный набор параметров.

        Чтобы получить доступ ко всем наборов параметров, следует прибегунть к полному объявлению

        Объявление формы полным методом напоминает объявление модели:
            1) В классе формы мы записываем атрибуты
            2) Во вложенном классе Meta мы записываем модель, которая должна быть привязана и список полей формы

        Параметры полей:
          label - Надпись для поля. (По умолчанию имя текущегополя)
          help_text - Поясняющий текст возле элемента управления
          label_suffix - добавляется к надписи для текущего поля
          initial - Начальное значение для поля формы
          required - Если True,то в поле обязательноолжно быть заненсено значение
          widget - элемент управления, которым будет преставлено поле на webстранице
          validators - Валидаторы текущего поля
          error_messages - сообщения об ошибках
          disabled - Если True, элемент будет недоступен

        Элементы управления:
          TextInput - обычное поле ввода
            ...
          HiddenInput - скрытое поле
            ...
          SelectDateWidget - поле ввода значения даты
"""
# Полное объявление всех полей формы
from django import forms
from .models import Poster, Rubric

class PosterForm(forms.ModelForm):
    title = forms.CharField(label='Название товара')
    content = forms.CharField(label='Описание', widget=forms.widgets.Textarea())
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric= forms.ModelChoiceField(queryset=Rubric.objects.all(),
                                   label='Рубрика',
                                   help_text='Не забудьте задать рубрику',
                                   widget=forms.widgets.Select(attrs={'size': 8}))
    class Meta:
        model = Poster
        fields = {'title', 'content', 'price', 'rubric'}

# Частичное объявление полей формы (урезанный функционал объявления)

class PosterForm2(forms.ModelForm):
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric= forms.ModelChoiceField(queryset=Rubric.objects.all(),
                                   label='Рубрика',
                                   help_text='Не забудьте задать рубрику',
                                   widget=forms.widgets.Select(attrs={'size': 8}))
    class Meta:
        model = Poster
# Порядок вывода, если не задать, то поля price и rubric из главного класса автоматически будут в конце
        fields = {'title', 'content', 'price', 'rubric'} 
        labels = {'title': 'Название товара'}