"""
	
		Библиотека Django Simple Captcha

			Для вывода искаженного изобажения при аутентификациях


			1) Установить
					pip install django-simple-captcha
					+Pillow 

			2) Добавить приложение
					INSTALLED_APPS = [
						...
						'captcha',
					]

			3) Выполнить миграции:
					manage.py migrate

					Библиотека создает таблицу
					captcha_captchastore

			4) В спске маршрутов проекта (urls.py) создать маршрут
					urlpatterns = [
						...
						path('captcha/', include('captcha.urls'))
					]
"""

"""
		
		Использование

			Чтобы использовать CAPTCHA, следует в форме объявить поле CapthcaField модуля captcha.fields.
		

"""
from django import forms
from captcha.fields import CapthcaField

# В формах, связанных с моделью
class CommentForm(forms.ModelForm):
	#...
	captcha = CapthcaField()
	class Meta:
		model = Comment

# В формах, не связанных с моделью
class PosterForm(forms.Form):
	#...
	captcha = CapthcaField(label='Введите текст с картинки', error_messages={'invalid': 'Неправильный текст'})


"""

		Натстройка Django Simple Captcha


			Часть натсроек (остальные можно прогуглить):
				CAPTCHA_CHALLENGE_FUNCT - полное имя функции, генерирующей текст в виде строки.
						В билиотеке доступны следующие функции:
							captcha.helpers.random_char_challenge - классика из 4 букв
							captcha.helpers.math_challenge - математическая (вычислить резульат выражения)
							captcha.helpers.word_challenge - Случайное слово из заданного словаря

						Пример:
						CAPTCHA_CHALLENGE_FUNCT = "captcha.helpers.word_challenge"

				CAPTCHA_LENGTH - Длина в символах текста для классической Captcha
				CAPTCHA_MATH_CHALLENGE_OPERATOR - строка с символом, обонач. оператор умножения.
					...
"""

"""
		
		Дополнительные команды 

			captcha_clean - удаляет из хранилища устаревшие CAPTCHA
				Пример:
					manage.py captcha_clean

			captcha_create_pool - Создает набор готовых CAPTCHA для дальнейшего использования.
				Формат:
					captcha_create_pool [--pool-size <кол-во создаваемых CAPTCHA>] [--cleanup-expired]
							--pool-size - кол-во предварительно создаваемых CAPTHCA (По умолчанию: 1000)
							--cleanup-expired - заодно удаляет устаревшие CAPTHCA
"""