"""

    Отпарвка писем админимтраторам и редакторам сайта:


        Настройки settings.py:

            ADMINS - список администраторов.

                ADMIN = [
                    ('Admin1', 'admin1@supersite.ru'),
                    ('Admin2', 'admin@othersite.ru'),
                    ('KingAdmin', 'megaadmin@megasite.ru')
                ]

            MANAGER - список редакторов.

            SERVER_EMAIL - адрес эл.почты отправителя, указываемый в письмах, что
                           отправляются админам и редакторам.
                           (По умолчаию: root@localhost)

            EMAIL_SUBJECT_PREFIX - префикс, доавляемый к темаам письма
                                   (По умолчанию: [Django])


        Для отправки писем для:
            1) Админимтраторов - применяется функция mail_admins()
            2) Редакторов - применяется функция mail_managers()

            mail_admins|mail_managers(<тема>,
                                      <тело>,[,
                                      fail_silently=False][,
                                      connection=None][,
                                      html_message=None])

                fail_silently - Если True, при ошибку будет возбуждено исключение SMTPException из smtplib

"""

# Пример:
from django.core.mail import mail_managers
mail_managers('Але, черти',
              'У вас прога сломалась',
              html_message='<strong>ДЭБИЛЫ, У вас прога сломалась</strong>')
