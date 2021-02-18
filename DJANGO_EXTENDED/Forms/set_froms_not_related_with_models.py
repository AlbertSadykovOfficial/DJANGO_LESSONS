"""
	
		Наборы форм, не связанные с моделями

			Создаются с помощью функции formset_factory() из django.forms

			formset_factory(form=<форма>[, 
											extra=1][,
											can_order=False][, can_delete=False][,
											min_num=None][, validate_min=False][,
											max_num=None][, validate_max=False][,
											formset=<набор форм>])
					<набор форм> должен быть подклассом класса BaseFormSet из модуля django.formsets

			Набор форм, не связанных с моделью, не поддерживают средств сохнранения занесенных в него данных.
			Атрибуты new_objects, changed_objects и delete_objects не доступны

			Класс набора форм, не связанного с моделю, имеет 2 полезных атрибута:
				ordered_forms - послеовательность форм, которые были переупорядочены
				deleted_forms - последовательность удаления форм

"""

# Пример создания набора форм:
from django.forms import formset_factory
fs = formset_factory(SearchForm, extra=3, can_delete=True)

# Конртроллер бработки набора форм
def formset_processing(request):
	FS = formset_factory(SearchForm, extra=3,  can_order=True, can_delete=True)

	if request.method == 'POST':
		formset = FS(request.POST)
		if formset.is_valid():
			for form in formset:
				if form.cleaned_data and not form.cleaned_data['DELETE']:
					keyword = form.cleaned_data['keyword']
					rubric_id = form.cleaned_data['rubric'].pk
					order = form.cleaned_data['ORDER']
					# Тут действия над данными
					# ...
					return render(request, 'board/process_result.html')
	else:
		formset = FS()
	context = {'formset': formset}
	return render(request, 'board/formset.html', context)
