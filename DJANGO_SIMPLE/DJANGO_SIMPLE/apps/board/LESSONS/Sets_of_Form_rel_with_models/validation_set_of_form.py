"""

	Валидация в наборах форм

		Уместо лишь тогда, когда необходимо проверить на правильность весь массив данных,
		введенных в этот набор.

		Валидация в наборе форм реализуется так:
			1) Объявляется класс производный от класса BaseModelFormSe из модуля django.forms
			2) В этом классе переопределяется метод clean(), котоырй отвечает за валидацию
			3) Выполняется создание класса набора форм путем спользования функции modelformset_factory()
				 Объявленный ранее класс указывается в параметре formset вызова этой функции

		Атрибуты forms, унаследованный от класса BaseModelFormSet хранит последовательностьвсех форм,
		что иеются в наборе. Сообщения об ошибках можно получиьт меодом non_form_errors()

"""

# Пример кода, выполняющего валидацию на уровне форм

class RubricBaseFormSet(BaseModelFormSet):
	def clean(self):
		super().clean()
		names = [form.cleaned_data['name'] for form in self.forms \
							if 'name' in form.cleaned_data]
		if ('Недвижимость' not in names) or ('Транспорт' not in names) or ('Мебель' not in names):
			raise ValidationError('Добавьте рубрикик недвижимости, ' + 'транспорта и мебели')
#...

def rubrics(request):
	RubricBaseFormSet = modelformset_factory(Rubric, fields=('name',),
																									can_order=True,
																									can_delete=True,
																									formset=RubricBaseFormSet
																					)
	#...