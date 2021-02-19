"""

    Настройки проекта, касающиеся разграничения достпупа

        AUTH_PASSWORD_VALIDATORS - список валидаторов, применяемых при введенении пароля при регистрации
        AUTHENTICATION_BACKEND - список классов, реализующих аутентификацию (в виде строк).
                                 По умолчанию: 'django.contrib.auth.backends.ModelBackend'
                                                реазалиузет аутент. и авториз. пользователей из списка модели
        AUTH_USER_MODEL - имя класса модели, зранящего список зарегистрированных пользовательей в виде строки.
                          По умолчанию: auth.User

"""