"""
    Шаблоны и статичские файлы (основы)

    Шаблон - образец для формирования web-страницы или электронной потчы...
    Шаблонизатор - подсистема фреймворка, формирующая окончательные web-страницы,
                   объединяя шаблоны и прелоставленные контроллерами контексты шаблонов, содержащие все нужные данные

    Шаблоны настраиваются в модуле settings.py в параметре TEMPLATES
    TEMPLATES - МАССИВ,каждый элемнт которого словарь

    В словаре ожно задать следующие элементы:
        BACKEND - путь к модулю шаблонизатора
                  В django: django.template.backends.django.DjangoTemplates - стандартный
                            django.template.backends.jinja2.Jinja2 - Jinja2
        NAME - псевдоним для шаблонизатора
        DIRS - всписок путей к папкам, в которых будет поиск шаблонов (по умолчанию "пустой список")
        APP_DIRS - True: Шаблонизатор дополнительно будет искать шаблоны в папках templates приложения
                   False: Шаблонизатор будет искать только в DIRS
        OPTIONS - Дополнительные параметры, поддерживаемые конкретными шаблонизаторами.
                  К примеру:
                    context_processors - список имен модулей, Реализующих обработчик контекста
                                         что должны использоваться совместно с заданным шаблонизатором
                    (Обработчик контекста - модуль, добавляющий в контекст шаблона каке-либо доп переменные
                                            уже после его формирования контроллером
                    )

        Обработчики контекста:
            django.template.context_processors.request -  добавляет в контекст шаблона переменную request,
                                                          хранящую объект текущего запроса
            django.template.context_processors.csrf    - доавляет в контекст шаблона жетон(токен)
            django.contrib.auth.context_processors.auth- Добавляет в контекст шаблона переменные user и perms,
                                                         хранящие сведения о текущем пользователе.
            django.contrib.messages.context_processors.messages - Добавляет в конекст шаблона переменные messages и
                                                                  DEFAULT_MESSAGE_LEVELS, хранящие список всплывающих
                                                                  сообщений и словарь, сопоставляюий строковые
                                                                  обозначения уровней сообщений с их числовым кодом.
            ....
            django.template.context_processor.tz - добавляет в контекст шаблона пееменную TIME_ZONE, хранящую
                                                   наименование текущей временной зоны

"""

# Настройки по умолчанию при создании проекта

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':    [],
        'APP_DIRS':True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ]
        }
    }
]
