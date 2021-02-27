"""

    Отключение кэширования

        При отправлке статических файлов, таких как css,
        Django уставнавливает большое время кеширвоания.
        При исправлении этих файлов мы из-за кэша не сможем
        увидеть их изменений.

        Решение:
         1) Очищать кэш после каждого изменения таблиц стилей
         2) Отключить кэширование

        Но можно указать Django, чтобы он не разрешал клиенту кэгирвать данне.
        ДЛЯ жтого в модуль urls.py пакета конфигураций добавляем:

            from django.contrib.staticfiles.view import serve
            from django.views.decorators.cache import never_cache

            urlpatterns = [
                # ...
            ]

            if settings.DEBUG:
                urlpatterns.append(path('static/<path:path>', never_cache(serve)))

        Если префикс STATIC_URL не по умолчанию (/static/), то значение path нужно изменить:
            urlpatterns.append(path('new_name/<path:path>', never_cache(serve)))

        После этого стоит очистить кэш браузера, чтобы он не продролжал исп. ранние копии.

        Затем запустить отлаочный сервер с ключом --nostatic:
            python manage.py runserver --nostatic

    !!! Как только работа над таблицами стилей будет закончена, рекомендуется вновь
        включить кэширвоаня статических файлов (закомментировать строки urls.py)


"""