"""

    Сессии

        Сессия - промежуток времени в течение которого посетитель пребывает на сайте.
                 Файлы сессии могут храниться в файлах или БД НА СТОРОНЕ СЕРВЕРА.
                 Пока не истечет промежуток времени, сессия считается актуальной

        Для каждой сессии Django генерирует идентификатор , который сохраняется в подписаном
        cookie на стороне клиента (cookie сессии).
        Содрежимое cookie, сохраненных для домена, АВТОМАТИЧЕСКИ отслыается в составе заголовков,
        их них можно извлечь ID сессии...

        Компоненты сессии:
          - django.contrib.sessions (INSTALLED_APPS)
          - django.contrib.sessions.middleware.SessionMiddleware (MIDDLEWARE)

        Параметры сессии в (settings.py)
          - SESSION_ENGINE - тип хранилища сессии
          - ... Разные параметры (сроки, имена, протоколы), надо - гугли
          - SESSION_FILE_PATH - полный путь к папке, в которм будут храниться файлы с сессиями.
          - SESSION_CACHE_ALIAS - название кэша, в котором будут хранится сессии.(default)


        Доступ:

            request.session['counter']

        Объект поддерживает различные методы:
            flush()  - удаляет все данные текущей сессии
            set_test_cookie() - создать тестовый cookie, чтобы проверить его поддержку в браузере
            delete_test_cookie()
                # ...
            clear_expired() - удаляет устаревшие сессии
            cycle_key() - создает новый ID для текущей сессии

        Команда clearsessions
            # Удаление всех устаревших сессий, которые не были удалены.
            python manage.py clearsessions
"""

# Пример проверки поддержки cookie

def test_cookie(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            # Поддерживает
        else:
            # Не поддерживает
    request.session.set_test_cookie()
    return render(request, 'main/test_cookie.html')