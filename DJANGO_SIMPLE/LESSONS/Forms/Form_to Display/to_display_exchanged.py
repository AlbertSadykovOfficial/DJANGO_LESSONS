"""
	Расширенный вывод форм

	Когда мы используем вывод формы по абзацам Шаблон (board/create.html),
	То между тегом label, создающим описание объекта, и элемента ввода по умолчанию ставится пробел.

	В Django есть возможность располагать отдельные элементы формы как нам хочется.

	Экземпляр класса ModelForm поддерживает функциональность словаря. Ключи совпадают с именами полей формы,
	значениями которых являются экземпляры класса BoundField, которые представляют поля формы в виде,
	доступном для помещения вшаблон.

	Если в директиве непосредственно указать экз. класса BoundField, он будет выведен как HTML-код,
	создающий элемент управления для текущго поля.

	# Вывести описание товара:
	
		{{ form.content }}
	
		Результат: <textarea name='content' id='id_content'></textarea>


		BoundFile поддерживает и други аттрибуты:
			label_tag (form.content.label_tag) 
				...
			errors (form.content.errors)
			non_field_errors (form.non_field_errors)
			...
"""