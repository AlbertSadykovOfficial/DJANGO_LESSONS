"""
    Сообщения об ошибках и обработка особых ситуаций:
    (При нештатных ситуациях) (Следует выдавать сообщения об ошибке)

 ++ Классы, представленные ниже, помогут самостоятельно обработать нештатную ситуацию
    Но Django обычно сам справляется

    Для выдачи ошибки Django предоставляет ряд классов, производных от HttpResponse

        HttpResponseNotFound([<содержимое>][,][content_type=None][,][status=404][,][reason=None])

        Пример:
            def detail(request, poster_id):
                try:
                    poster = Poster.objects.get(pk=poster_id)
                except Poster.DoesNotExist:
                    return HttpResponseNotFound('Такое объявление не существует')

                return HttpResponse(...)

        Или:
            def detail(request, poster_id):
                try:
                    poster = Poster.objects.get(pk=poster_id)
                except Poster.DoesNotExist:
                    return Http404('Такое объявление не существует')

                return HttpResponse(...)

        # Клиентский запрос некорректно сформирован:
        HttpResponseBadRequest([<содержимое>][,][content_type=None][,][status=400][,][reason=None])

        # Доступ к странице запрещен (не выполнен вход, к примеру):
        HttpResponseForbidden([<содержимое>][,][content_type=None][,][status=403][,][reason=None])
            # Так же можно возбудить Искл: PermissionDenied

        # Запрос выполнен с применением недопустимого метода
         HttpResponseNotAllowed([<последовательнось обозначений разрешенных методов>][,][content_type=None][,][status=405][,][reason=None])
        Пример:
            return HttpResponseNotAllowed(['GET'])

        # Запрошенная страница более не существует:
        HttpResponseGone([<содержимое>][,][content_type=None][,][status=410][,][reason=None])

        # Ошибка в программном коде сайта
        HttpResponseServerError([<содержимое>][,][content_type=None][,][status=500][,][reason=None])

        # Страница не изменилась с момента последнего запроса
        HttpResponseNotModified([<содержимое>][,][content_type=None][,][status=304][,][reason=None])

"""