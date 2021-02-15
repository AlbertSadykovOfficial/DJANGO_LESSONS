"""
	Обработка наборов форм, связанных с моделями

		Набор форм обрабатывается самостоятельно, без возможностей django (как при исп высокоуровневых контроллеров)

		Логика такая же как и при одиночных формах: 
			1) При получении GET-запросв, нужно создать объект набора форм
			2) Добавить его в контекст шаблона
			3) Отрендерить его
		
		Создать набор форм:
			formset = RubricFormSet()
			Параметры:
				-initial - начальные данные, которые помещаются в пустрый формы
				-queryset - набор записей, откуда будут взяты записи для вывода набора форм
"""

# Вывести в наборе первые 5 значений

formset = RubricFormSet(initial=[{'name': 'Новая рубрика'},
																 {'name': 'Еще одна новая рубрика'}],
																 queryset = Rubric.objects.all()[0:5])

# Обработка запроса после получения ответа от польователя:
formset = RubricFormSet(request.POST)
formset = RubricFormSet(request.POST, queryset=Rubric.objects.all()[0:5])

# После получения формы, следует провести ее валидацию
if formset.is_valid():
	formset.save() # Возвращает пооследовательность вех записей модели, что представлены в наборе форм

# После вызова save() мы можем воспольоваться 3 атрибутами:
#  new_objects -  последовательность добавленных записей
#  changed_objects- последовательность измененных записей
#  delete_objects - последовательность удаленных записей (при выставленном параметре can_delete)
#
# Есть параметр commit, при значении False, помеченные на удаление файлы удалены не будут
# Придется перебирать все удаленные записи, что находятся в списке deleted_objects и вызвать у каждой метод delete
formset.save(commit=False)
for rubric in formset.deleted_objects: 
	rubric.delete()

# Атрибут cleaned_data возвращает словарь занесенных в форму данных
# Если в форму не занесены данные, словарь будет пустым

for form in formset:
	if form.cleaned_data:
		# Форма не пуста, и мы можемполучить занесенные в нее данные


# Полный код контроллера-функции, обрабатывающего набор форм:
from django.shartcuts import render, redirect
from django.forms import modelformset_factory
from .models import Rubric

def rubrics(request):
	RubricFormSet = modelformset_factory(Rubric, 
																				fields=('name',), 
																				can_delete=True)
	# Если пришла заполненная форма
	if request.method = 'POST':
		formset = RubricFormSet(request.POST)
		if formset.is_valid():
			formset.save()
			return redirect('board:index')
	else:
		formset = RubricFormSet()
	context = {'formset': formset}
	return render(request, 'board/rubrics.html', context)

# В Django не реализовано упорядочивание записей и набор форм е сохраняет порядковые номера в моделях,
# Поэтому его нунжо реализовывать самостоятельно
# 
# Для реалиации следует добавить новое поле в класс Rubric, которое будет хранить порядок: order
# 
# class Rubric(models.Model):
#			...
#		order = models.SmallInteger Field(default=0, db_index=True)
#			...
#		class Meta:
#				...
#			ordering = ['order', 'name']
# 

# Полный код контроллера-функции, обрабатывающего набор форм:
from django.shartcuts import render, redirect
from django.forms import modelformset_factory
from django.forms.formsets import ORDERING_FIELD_NAME
from .models import Rubric

def rubrics(request):
	RubricFormSet = modelformset_factory(Rubric,
																			 fields=('name',),
																			 can_order=True,
																			 can_delete=True)
	# Если пришла заполненная форма
	if request.method = 'POST':
		formset = RubricFormSet(request.POST)
		if formset.is_valid():
			for form in formset:
				if form.cleaned_data:
					rubric = form.save(commit=False)
					rubric.order = form.cleaned_data[ORDERING_FIELD_NAME]
					rubric.save()
			return redirect('board:index')
	else:
		formset = RubricFormSet()
	context = {'formset': formset}
	return render(request, 'board/rubrics.html', context)