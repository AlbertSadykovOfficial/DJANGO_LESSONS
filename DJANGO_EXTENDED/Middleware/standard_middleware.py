"""

    Стандартные посредникики

        Помимо стандартных еще есть:
            django.middleware.gzip.GZipMiddleware - сжимает страницу алгоритмом gzip, если размер > 200 Байтов,
                                                    а web-обозреватель поддерживает сжатие страниц

                                                    В списке MIDDLEWARE должен находится перед теми, кто получает
                                                    доступ к содержимому ответа с целью прочетния или изменения его.

            django.middleware.http.ConditionalGetMiddleware - обработка заголовков, связанных с кэшированием страниц
                                                              на уровне клиент. Если ответ не имеет заголовка E-Tag,
                                                              такой заголовок не будет добавлен.
                                                              Если будет, отправит 304 страницу

                                                              В списке MIDDLEWARE должен находится перед:
                                                              django.middleware.common.CommonMiddleware

            django.middleware.cache.UpdateCacheMiddleware - обновляет кэш при включенном режиме кэширования сайта.
                                                            В списке MIDDLEWARE должен находится перед теми,
                                                            кто модифицирует аголовк Vary:
                                                                django.contrib.sessions.middleware.SessionMiddleware
                                                                django.middleware.gzip.GZipMiddleware

            django.middleware.cache.FetchFromCacheMiddleware - извлекает запрошеную страницу из кэша при включенном
                                                               режиме кеширования сайта.
                                                               В списке MIDDLEWARE должен находится перед теми,                                                               В списке MIDDLEWARE должен находится перед теми,
                                                               кто модифицирует аголовк Vary:
                                                                 django.contrib.sessions.middleware.SessionMiddleware
                                                                 django.middleware.gzip.GZipMiddleware

"""