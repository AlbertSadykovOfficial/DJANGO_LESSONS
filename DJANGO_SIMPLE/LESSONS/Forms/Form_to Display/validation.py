"""
	Валидация в формах

		Помимо того, что можно выполнять валиацию на уровне отдельных полей и всей модели,
		Мы можем также реализовывать валидацию на уровне форм, связнанных с моделью

"""

# Валидация с применением валидаторов
	from django.core import validators

	class PosterForm(forms.ModelForm):
		title = forms.CharField(label='Название товара',
														validators=[validators.RegexValidator(regex='^.{4,}$')],
														error_messages={'invalid': 'Неправильное название товара'})


# Валидация путем переопределения методов формы:
# Если требуетс более сложная проверка, то следует переопрделить метод в классе формы
# Название следует указывать: clean_<имя поля>
# Метод не должен принимать параметров и должен возвращать значение проверяемого поля:

class PosterForm(forms.ModelForm):
	def clean_title(self):
		val = self.cleaned_data['title']
		if val == 'Бракованный товар':
			raise ValidationError('Бракованный товар нельзя продавать')
		return val

# Полная валидация формы (clean):

class PosterForm(forms.ModelForm):
	...
	def clean(self):
		super().clean()
		errors = {}
		if not self.cleaned_data['content']:
			errors['content'] = ValidationError('УКАЖИТЕ ОПИСАНИЕ ТОВАРА')
		if self.cleaned_data['price'] < 0:
			errors['price'] = ValidationError('Цена не может быть отрицательной')
		if errors:
			raise ValidationError(errors)