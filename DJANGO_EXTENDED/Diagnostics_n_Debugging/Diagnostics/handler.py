"""

    Обработчики

        Выполняют вывод сообщений в поддреживаемые ими устройства:
        Консоль, Файл, и т.д.

        Перечень обработчиков записывается в том же выиде, что и перечень форматировщиков.

        Параметры обработчика:
            class - строка с именем класса обработчика
            level - минимальный уровень сообщений в виде строки
            formatter - форматировщик
            filters - список фильтров, через которые будут прохожить выводимые обработчиком сообщения.


        Наиболее часто используемые классы обработчика:
            logging.StreamHandler - выводит сообщение в консоль
            logging.FileHandler(filename=<путь к файлу>[,
                                mode='a'][,                 # Режим открытия файла
                                encoding=None][,            # Кодировка
                                delay=False]) # True - открывается в момент вывода сообщения
                                              # False - в момент инициализации класса
                                 - сохраняет сообщение в файле с заданным путем.
            logging.handlers.RotatingFileHandler - что и FileHandler, но вместо 1 файла, создает
                                                   несколько файлов заданного размера
            logging.handlers.TimedRotatingFileHandler - что и RotatingFileHandler,
                                                    но вместо 1 файла, использует несколько,
                                                    которые создаются через заданный промежуток времени.
            django.utils.log.AdminEmailHandler([include_html=False][,][email_backend=None])
                (Отправляет сообщение по электронной потче по адресам, приведенным в списке ADMINS)
            logging.handlers.SMTPHandler - отправляет сообщения по эл. почте на произвольный адрес.
            logging.NullHandler - не выводит сообщения.



"""

# Пример
LOGGING = {
    # ...
    'handlers': {
        'console_dev': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['require_debug_true'],
        },
        'file': {
            'class': 'logging.handler.RotatingFileHandler',
            'filename': 'd:/django-site.log',
            'maxBytes': 1048576,  # 1 Mb
            'backupCount': 10,
            'formatter': 'simple',
        },
        #...
    }
}