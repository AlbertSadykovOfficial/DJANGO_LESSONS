"""

    Получение сведений о пользователе

        Любой зарегистрированный пользователь предсавляется вDjango классом User модля django.contrib.auth.models

        Получить доступ к экз класса User, представляющего текущего пользователя:

            В контроллере:
            def index(request):
                if request.user.is_authenticated:
                    ...

            В шаблонне:
            {% if user.is_authenticated %}
                ...
            {% endif %}

        Атрибуты поля и методы класса User:
            username
            password
            email
            first_name
            last_ame
            is_active
            is_staff - Пользователь имеет статус персонала
            is_superuser
            groups - группы, в которые входит

            last_login - дата и время поседнего входа
            date_joined - дата и время регистрации

            is_anonymous - Если вход на сайт еще не выполнен

            has_perm(<право>[, obj=None]) - True, если имеет указанное права
            has_perms(<права>[, obj=None]) - True, если имеет все права для пользователя

            get_username() - имя пользователя, которое он наюирает для входа на сайт
            get_full_name() - возвращает имя+фамили, разделенную фпробелом

            get_short() - настоящие имя пользователя
"""