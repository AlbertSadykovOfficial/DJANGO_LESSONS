"""
    Cookie

        Cookie - инструмент для сохранения данных (< 4 Кбайт) на стороне клиента

        Все cookie хранятся в массиве COOKIES объекта запроса HttpRequest

            request.COOKIES['counter']

        Записать значение в COOKIE:
        set_cookie(<ключ>[,    # Строка
                    value=''][,
                    max_age=None][, # Время хранения в секнудах
                    expires=None][, # Дата  время после которых cookie станет не действительным
                    path='/'][,     # путь к cookie (привязка их к пути запроса)
                    domain=None][,  # Домен, откуда должен быть доступен cookie
                                    # (если нужно создать cookie доступный с другого домена)
                                    # www.site.ru support.site.ru
                    secure=None][,  # True - будут работать только по защищенному протоколу
                    httponly=False][, # Только по http и https протоколам
                    samesite=None]) # Разрешить отправку cookie при обращении на др. сайты.

        Пример:
            response = HttpResponse(...)
            response.set_cookie('counter', cnt)

        Подписанные cookie:
        set_signed_cookie(<ключ>[, value=''][,
                            salt=''][,  # salt -значение для генерированяцифрововй подписи
                            #...
                        )

        Получить значение подписанных cookie:
        # (salt должно быть идентичным, что и в set_signed_cookie)
        # Если произошла копмрометация -> RAISE_ERROR
        get_signed_cookie(<ключ>[, default=RAISE_ERROR][, salt=''][, max_age=None])


        Удалить cookie:
        # (path и cdomain должны юыть как и при установке )
        delete_cookie(<ключ>[, path='/'][, domain=None])

"""