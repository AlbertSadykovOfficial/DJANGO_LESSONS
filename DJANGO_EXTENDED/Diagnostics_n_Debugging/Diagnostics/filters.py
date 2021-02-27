"""

    Фильтры:

        Фильтр отбирает ля вывода только те сообщения, котторые удовлетворяют определнным условиям,
        или выводить сообщение, если выполнится какое-либо условие, не связанное с сообщением

        Классы фильтров, предлагаемые Django, оъявлены в модуле django.utils.log:
            RequireDebugTrue - вывести сообщение, если включен отладочный режим
            RequireDebugFalse - вывсти сообщение, если включен эксплуатационны режим.
            CallbackFilter(callback=<функция>) - отбирает только те сообщения, для которых
                                                 указанная в пармаметре функция вернет (True)
                                                 Укзанная функция должна принимать единственный
                                                 параметр - сообщ, представл. LogRecord


"""

LOGGING = {
    'filters': {
        'required_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'required_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
}

# Пример CallbackFilter

def info_filter(message):
    return message.levelname == 'INFO'

LOGGING = {
    # ...
    'filters': {
        'info_filter': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': info_filter,
        },
    },
    # ...
}
