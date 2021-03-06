"""
    Контроллеры - функции

    Контроллеры - программные модули, выполняющие все работы по:
        1) выборке данных из Базы
        2) подготовки их для вывода
        3) Обработки данных от посетителя
        4) Сохранению обработанных данных в БД.
        5) Формированию веб-страниц
    (реализуют основню часть логики сайта)


 Введение:
    К.ф. - обычные функции python, которые обязаны принимать:
        1) Экземпляр класса HttpRequest (django.http) - request
        2) Набор именованных параметров, (имена совпадают с именами URL-параметров,
                                          объявленных в связном с контроллером маршруте)

    К.ф. должен возвращать экземпляр класса HttpResponse (django.http)
    Код контроллеров предполагается располагать в файле views.py, но можно и в другое место.
"""