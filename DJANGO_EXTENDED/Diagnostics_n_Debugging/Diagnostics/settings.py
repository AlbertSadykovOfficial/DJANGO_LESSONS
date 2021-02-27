"""

    Настройка средств диагностики (settings.py)

        settings.py -> словарь LOGGING

        Параметры:
            version - № версии стандарта, а котором записываются настройки средств диагностики
            formatters - Определет формат, в котором будет представлено каждое сообщение об ошибке и т.д.
            filters - Отбирают для вывода только те сообщения, которые удоавлетворяют условим.
            handlers - выполняют вывод сообщений определенным способом (консоль, файл, письмо)
            loggers - собирает все сообщения, отправленные какой-либо подсистемой Django
            disable_existing_loggers - True, средсва диагностики, исп по умолчанию, работать не удут.

"""

# ПРИМЕР настройки диагностических средств
#
# Результат:
#   + Если вкл. (отлад.) реж. в консоли будут выводиться все сообщения
#   + Если вкл. (экспл.) реж. в консоле будут выводиться только сообщения о крит. ошибках
#
#
# disable_existing_loggers = True  - Отключить все средства диагностики по умолчанию
#
# Форматировщик simple будет выводить сообщения типа:
# [<дата и время создания>] <уровень>: <текст>.
#
# Обарботчики
# console_dev - выводить в носоль сообщения любого уровня, прошедших через required_debug_true
# console_prod - будет выводить в консоль сообщения уровня ERROR, прошедших через required_debug_false
# file - сохранять в файл сообщения любого уровня (при превышении файла 1M, создаст новый)
#
# Регистраторы
# django - собирает сообщения из всех подсистем и выводит их через console_dev и console_prod
# django.server - собирает все сообщения ур-я INFO и выше, когда запущен отладочный сервер
# и выводит их в обработчик file

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'required_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'required_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s%] %(levelname)s: %(message)s',
            'datefmt': '%Y.%m.%d %H:%M:%S',
        },
    },
    'handlers': {
        'console_dev': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['require_debug_true'],
        },
        'console_prod': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'ERROR',
            'filters': ['require_debug_false'],
        },
        'file': {
            'class': 'logging.handler.RotatingFileHandler',
            'filename': 'd:/django-site.log',
            'maxBytes': 1048576, # 1 Mb
            'backupCount': 10,
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console_dev', 'console_prod'],
        },
        'django.server': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}