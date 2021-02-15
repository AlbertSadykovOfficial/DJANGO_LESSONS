"""

	Обработка форм

	Объявив класс формы, мы можем использовать его для обработки и сохранения полученных данных.

	Если используются высокоуровневые классы, то они сами выполняет сохранение данных.
	Напротив, если используются низкоуровневые классы или функции, то придестя делать все самим.

		Чтобы добавить запись, нужно созать экземляр класса, поместить его в контекст шаблона и 
		выполнить рендеринг шаблона.
"""

# Создать:
	posterForm = PosterForm()

# Поместить в форму изначальные данные (ПРИСВАИВАЕМ словарь, где ключи-имена полей формы, а значения-значения)
	posterForm = Poster(initial={color='red'})

# Поместить в форму данные, полученные в составе запроса:
	posterForm = PosterForm(request.POST)

# Вальдация данных:
	valid = posterForm.is_valid():

# Получить сведения об ошибках при валидации:
	if posterForm.errors:
		#	Список ошибок, допущенных при вводе названия товара
		title_errors = posterForm.errors['title']
		# Список ошибок, относящийся ко всей форме
		form_errors = posterForm.errors[NON_FIELDS_ERRORS]
	else:
		# Данные корректны (можно снова вывести странцу)

"""
	Сохранение данных, занесенных в форму save()

		Перед сохранением рекомендуется выполнить валидацию,
		если ее не выполнить save() сама это сделает и в случае,
		если проверка не успешна, то вызовется исключение:
			ValueError
"""
	
# Метод save() в результате возвращает объект созданной или исправленной записи модели.
# Есть возможность получить созданную, но не сохраненную запись модели с целью внемения правок,
# сделать это можно, испольховав при вызове метода параметр commit и присвоить ему False
			
	poster = PosterForm.save(commit=False)
		
# После этого с записью можно произвести действии сохранить обычным методом:
	if not poster.color:
			poster.color = 'red'
	poster.save()

# При сохранении записи модели многие со многоими, нужно учитывать, что 
# Чтобы связь меду записями была успешно создана, связываемая запись должна иметь ключ
# (именно ключ связываемой записи записывется в связующей таблице)
# Пока запись НЕ СОХРАНЕНА, ключа НЕТ
# Поэтому сначала нужно сохранить запись вызовом метода save() у самой модели,
# --> потом создать связь вызововом save_m2m()

mf = MachineForm(request.POST)
if mf.is_valid():
	machine = mf.save(commit=False)
	# Выполняем доп действия c записью
	machine.save()
	mf.save_m2m()

"""
	Доступ к данным формы

	Допустим, надо достать данные в только что введенную форму для перенаправления,
	это можно осуществить, используя аттрибут cleaned_data
		posterForm.cleaned_data['rubric'].pk
"""

#  Пример перенаправления (../../Controllers_functions/how_to_build.py):
	return HttpResponseRedirect(reverse('board:by_rubric', kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))

"""
	Правка записи посредством формы:

		1) Создать форму при правке записи
		2) Вывести страницу с формой
		3) После получения запроса, создать форму в второй раз,
			 указав первым параметром полученные данные POST, вторым instance=исправляемую запис
		4) Выполнить валидацию формы

	 Метод has_changed(), котоырй возвращает True, если данные формы были изменены.

"""

# Правка записи с ключом pk, полученным через GET-парметр

def edit(request, ok):
	poster = Poster.objects.get(pk=pk)
	if request.method == 'POST':
		posterForm = PosterForm(request.POST, instance=poster)
		if posterForm.is_valid():
			posterForm.save()
			return HttpResponseRedirect(reverse('board:by_rubric', kwargs={'rubric_id': posterForm.cleaned_data['rubric'].pk}))
		else:
			context = {'form': posterForm}
			return render(request, 'board/poster_form.html', context)
	else:
		posterForm = PosterForm(instance=poster)
		context = {'form': posterForm}
		return render(request, 'board/poster_form.html', context)

"""
	Удаление записи

		1) Извлечь запись для удаления
		2) Вывести на экран страницу с предупреждением
		3) Произвести удаление (POST)

"""

def delete(request, pk):
	poster = Poster.objects.get(pk=pk)
	if request.method == 'POST':
		poster.delete()
		return HttpResponseRedirect(reverse('board:by_rubric', kwargs={'rubric_id': poster.rubric.pk}))
	else:
		context = {'poster': poster}
		return render(request, 'board/poster_confirm_delete.html', context)