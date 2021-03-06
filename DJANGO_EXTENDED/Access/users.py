"""

    Работа с пользователями

        Создать пользователя

        create_user(<имя>, password=<пароль>[,
                    email=<адрес>][,
                    <доп поля>])
            Создает нового пользователя с именем и паролем, доп поля созраняются в модли пользователя


        create_superuser(<имя>, <адрес эл. почты>, <пароль>, <доп поля>]) - созданный пользователь становится активным,
                        выполняется его сохранение и он возвращается в качестве результата

        Работа с паролями

            check_password(<пароль>) - True, если пароль совпадает с ранящимся в списке
                Пример:
                    admin = User.objects.get(name='admin')
                    if admin.check_password('password'):
                        # пароли совпадают

            set_password(<новый пароль>) - задает для ТЕКУЩЕГО польователя НОВЫЙ пароль, но СОХРАНЕНЕНИЕ НЕ ВЫПОЛНЯЕТ:
                Пример:
                    admin.set_password('newpass')
                    admin.save()

            set_unusable_password() - задае текущего пользователья недействительный пароль. При проверке такого пароля
                                      функцией check_password, она вернет False

            has_usable_password() - True, если для текущего пользователя был задан текущий пароль и False, если пароль
                                    недействителен

"""