"""

    Всплывающие сообщения

        Существуют тольоко во время текущего запроса, предназначениы для вывода сообщения
        актуального только в данный момент (к примеру, успешное добавление записи)


        Настройка:
            - django.contrib.messages (INSTALLED_APPS)
            - django.contrib.sessions.middleware.SessionMiddleware (MIDDLEWARE)
            - django.contrib.sessions.middleware.MessageMiddleware (MIDDLEWARE)
            - django.contrib.messages.context_processors.messages

        Параметры всплывающих сообщений в (settings.py)
            MESSAGE_STORAGE - класс, реализующий хранение сообщений, представленных в виде строки
            MESSAGE_LEVEL - минимальный уровень всплыающих сообщений, которые будут выводиться подсистемой.
            MESSAGE_TAG - соотв. между уровнями сообщений и стелевыми классами

        Уровни всплывающий сообщений:
            Уровень выражается целым числом, изначально в django 5 уровней, каждый из которых имеет
            определенную область применения. Значения занесены в переменные,
            хранящиеся в (django.contrib.messages)

            Пареметр MESSAGE_LEVEL - узказывает МИНИМАЛЬНЫЙ УРОВЕНЬ, КОТОРЫЙ БУДЕТ ОБРАБОТАН
            Если указан 20 (INFO), значения 10 (DEBUG) обарбатываться неп будут

                Переменная  |Val | Описание                                 | Класс
                   DEBUG    | 10 | Отлдочные сообщения (для разработчикков) | debug
                   INFO     | 20 | Информационое сообщение для поситителей  | info
                  SUCCESS   | 25 | Сообщение об успешном выполнении действий|success
                  WARNING   | 30 | Нештатная ситуация, ведущая к сбою       |warning
                   ERROR    | 40 | Неуспещное выполнение действия           | error

        Создание сообщений:
            add_message(<запрос>, <уровень сообщения>, <текст сообщений>[, extra_tags=''][, fail_silently=False])

                Запрос - экз. класса HttpRequest
                Уровень - целое число
                Текст - строка сообщения
                extra_tags - дополнительные стилевые классы (строка, классы отделятся пробелами)
                fail_silently - True, в случае невозможности создания сообщения ничего не произойдет,
                                По умолчанию возбудится MessageFailure

            Пример:

                def edit(request, pk):
                    messages.add_message(request,
                                         message.SUCCESS, 'объявление исправлено',
                                         extra_tags='first second')
                # или
                debug|info|success|warning|error(<запрос>,<текст сообщения>[,...])
                message.success(request, 'Объявление испрвлено')

        Добавить поддерку всплывающих сообщений высокоуровневым классам можно,
        унаследовав их от класса-примеси SuccessMessageMixin,
        который объявлен в модуле django.contrib.messages.views

            Атрибут и метод класса:
            success_message - текст сообщения об успешом выполнении операции.
            get_success_message(<словарь с данными формы>) - выдает сформированный текст вспл. сообщ.

        Пример:
            class PosterCreateView(SuccessMessageMixin, CreateView):
                template_name = 'board/create.html'
                form_class = PosterForm
                success_url = '/{rubric_id}'
                success_message = 'Объявление о продаже товара "% (title)s" создано.'


        Вывод всплывающий сообщений:

            В шаблоне удобно использовать django.contrib.messages.context_processors.messages
            Он добавляет в контекст шалона переменную messages, ранящую последовательность
            всех всплывающих сообщений

                message - текст всплыващего сообщения
                level - уровень всплывающего сообщения
                level_tag - имя основного стилевого класса, соотв. уровню сообщения
                extra_tags - строка с доп стилевыми классами
                tags - строка со всеми стилевыми классами

                + переменая-словарь (уровни сообщений):
                    DEFAULT_MESSAGE_LEVELS
                    --> DEFAULT_MESSAGE_LEVELS.ERROR

            Пример шаблона:

            {% if messages %}
            <ul class="messages">
                {% for message in messages %}
                <li{% if message.tags %} class="{{ message.tags }}" {% endif %}>
                    {{ message }}
                </li>
                {% endfor %}
            </ul>
            {% endif %}

            Переменая-словарь DEFAULT_MESSAGE_LEVELS
            {% if message.level == DEFAULT_MESSAGE_LEVELS %}
                #...
            {% endif %}


        Если нужно получить доутсп к сообщениям в контроллере,
        можно воспользоваться get_messages(<запрос>) (из django.contrib.messages)

            Запрос - HttpRequest

        Пример:
            def edit(request, pk):
                messages = messages.get_messages(request)
                first_message_text = messages[0].message


        Объявление своих уровней всплывающий сообщений

        CRTICAL = 50
        messages.add_message(request, CRITICAL, 'Очень плохо')

        Чтобы использовать стилевой класс, добавим в настроки проекта слежующий словарь

        MESSAGE_TAGS = {
            CRITICAL: 'critical'
        }
"""