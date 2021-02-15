"""

	Встроенные наборы форм

		Служат для работы с наборами записей вторичной модели, связанными с указаной 
		записью первичной модели


		Создание
			inlineformset_factory(<первичная модель>, <вторичная модель>[,
														form=<форма, связанная с моделью>][,
														fk_name=None][, # Имя клчевого поля вторичной модели по которому идет связь с первичной
														fields=None][,
														exclude=exclude][,
														labels=None][,
														help_text=None][,
														error_messages=None][,
														field_classes=None][,
														widgets=None][,
														extra=3][, # Кол-во пустых форм
														can_order=False][,
														can_delete=True][,
														min_num=None][,validate_min=None][,
														max_num=None][,validate_max=None][,
														formset=<набор форм, связанных с моделью>])

		Обработка встроенных наборов форм 
		
		Так же как и для обычных наборов форм, 
		но нужно передавать конструктору с параметром instance запись первичной модели,
		после этого наор форм выведет записи вторичной модели, связанные с этой записью

"""

# Код контроллера, который выводит выводит на экран страницу со встроенным набором форм

from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from .models import Poster, Rubric
from .forms import PosterForm

def posterForms(request, rubric_id):
	posterFormSet = inlineformset_factory(Rubric, Poster, form=PosterForm, extra=1)
	rubric = Rubric.objects.get(pk=rubric_id)
	if request.method == 'POST':
		formset = PosterFormSet(request.POST, instance=rubric)
		if formset.is_valid():
			formset.save()
			return redirect('board:index')
		else:
			formset = PosterFormSet(instance=rubric)

		context = {'formset': formset, 'current_rubric': rubric}
		return render(request, 'board:poster_form')