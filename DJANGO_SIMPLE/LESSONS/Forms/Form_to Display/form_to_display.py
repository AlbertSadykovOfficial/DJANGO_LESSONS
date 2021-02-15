"""
	Быстрый вывод форм
		
		as_p - по абзацам
		as_ul - в виде маркированного списка
		as_table - в виде таблицы

		Пример:
		<form method='post'>
			{% csrf_token %}
			<table>
				{{ form.as_table }}
			</table>
			<input type='submit' value='Добавить'>
		</form>
"""

"""
	Формат данных

		По умолчанию: application/x-www-form-urlencoded

		Чтобы отправлять файлы, нужно укзаать multipart/form-data
		Метод is_multipart() - возвращает True,если форма содержит поля, предназначеные для хранения файлов:

		{% if form.is_multipart %}
			<form enctype="multipart/form-data" method="post">
		{% else %}
			<form method="post">
		{% endif %}
"""