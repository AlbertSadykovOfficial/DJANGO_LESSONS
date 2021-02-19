"""

    Аутентификация и выход с сайта

        Аутентификация проходит в 2 этапа:
            1) Поиск пльзователя в списке
            2) Вход

        Понадобится 3 функции из модуля django.contrib.auth:

            authenticate(<запрос>, username=<имя>, password=<пароль>)
                запрос - HttpRequest

                Если пользователь с указанным именем и паролем существует,
                То функция возвзращает объект пользователя User,
                Иначе None

            login(<запрос>, <пользователь>)
                запрос - HttpRequest
                пользователь - запись модели User

            logout(<запрос>)
                запрос - HttpRequest
"""

from django.contrib.auth import authenticate, login, logout

def my_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

def my_logout(request):
    logout(request)
    # выход выполнен, выполняем перенаправление