"""

    Теги шаблонизатора

    Теги управляют геенерированием  содержимого

    Одинарный тег:
        {% csrf_token %}

    Парный тег (охватывает другие фрагменты кода)
        {% for poster in posters_pull %}
            ...
        {% endfor %}

    Некоторые теги, поддреживаемые шаблонизатором Django:
        url : {% url 'board:detail' poster.pk %}
        load - загружает библиотеки тегов
                {% load static %}
        ifchanged - выводит содержимое, если оно изменилось после предыдущей итерации цикла (работает в цикле):
            {% ifchanged %}  <содержимое>  {% endifchanged %}
            {% ifchanged <список значений, разделенных пробелами> %}
                <содержимое>
            {% endifchanged %}
            Пример:
            {% for rubric in rubrics %}
            {% ifchanged rubric.parent %}
                {{ rubric.parent.name}}
            {% endifchanged %}
            {% endfor %}
        ...
        firstof <список, разделенный проблеми> - помещает первое непустое значение из списка:
            {% firstof poster.phone poster.email 'Отпправить' %}
        ...
        now <формат> - всавляет текущее значение даты и времени
            {% now 'SHORT_DATETIME_FORMAT' %}

        filter - применяет к содержимому указанные фильтры
            {% filter force_escape|upper %}
                <p>Текст тега filter</p>
            {% endfilter %}

        autoescape on|off endautoescape - Автоматическое преобразование недопустимых HTML-тегов
        spaceless - удаляет пробельные символы(Табуляцию...)
        verbatim - вставлвляет содержимое как есть, не обрабатывая в нем директивы, теги и фильтры шаблнизатора
                {% verbatim %}
                    <p> Тег времени в Django: {% now %}</p>
                {% endverbatim %}

        comment - помещает в код комментарй, который не бует обрабатываться шаблонизатором:
            {% comment 'не забудь исправить' %}
                <p>Здесь будет список объявлений</p>
            {% endcomment %}

        debug - вывести отладочную информаицю

"""
