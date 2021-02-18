"""

		Формы, не связанные с моделями

			Могут понадобиться для обработки данных до занесения их в БД 
			И для данных, которые вообще не нужно заносить в БД

			Особенности:
				1) Форма объявляется как подкласс Form из django.forms
				2) Все поля, которые должны присутствовать в форме, необходимо
					объявить в виде атриибутов класса формы
				3) Вложенный класс Meta в такой форме не объявляется (т.к этот класс предназначен для сведений модели)
				4) Средства хранения введенных в форму данных (instance, save()) не поддерживаются
			
"""

# Пример объявления не связанной с моделью формы
from django.forms import forms

class SearchForm(forms.Form):
	keyword = forms.CharField(max_length=20, label='Искомое слово')
	rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Рубрика')


# Контроллер извлечения данных
def search(request):
	if request.method == 'POST':
		sf = SearchForm(request.POST)
		if sf.is_valid():
			keyword = sf.cleaned_data['keyword']
			rubric_id = sf.cleaned_data['rubric'].pk
			poster = Poster.objects.filter(...)
			context = {'poster': poster}
			return render(request, 'board/search_result.html', context)
	else:
		sf = SearchForm()
	context = {'form': sf}
	return render(request, 'board/search.html', context)