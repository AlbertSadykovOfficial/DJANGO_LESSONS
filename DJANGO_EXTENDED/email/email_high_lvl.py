"""

    Высокоуровневые инструменты для отправки писем

        Если нет небходимости создавать письма с вложениями,
        можно воспользоваться высокоуровневыми средствами отправки писем.


    Отправка писем по произвольным адресам

        send_mail() - отправляет 1 письмо по укзааныым адресам
            send_mail(<тема>,
                      <тело>,
                      <адрес отправителя>,
                      <адрес получателей>,[,
                      fail_silently=False][,
                      auth_user=None][,
                      auth_password=None][,
                      connection=None][,
                      html_message=None])

            auth_user, auth_password - логин пароль для поклчеия к SMTP-серверу

        send_mass_mail() - выполняет отправку писем из указанного перечня.
            send_mass_mail(<перечень писем>,[,
                           fail_silently=False][,
                           auth_user=None][,
                           auth_password=None][,
                           connection=None]
                           )


    Отправка писем зарегистрированным пользователям:

        Мы можем отпарвлять письмо любому зарегистрированному пользователю,
        для того класс User предоставляет метод email_user(),
        все переданные в функцию параметры будут переданы функции send_mail():

            email_user(<тема>, <тело>[, from_email=None][, <доп параметры>])

"""
# Отправка писем по произвольным адресам
from django.core.mail import send_mass_mail
msg1 = ('Подписка', 'Подтвердите, пожалуйста, подписку',
        'subscripe@mail.ru',
        ['user1@mail.ru', 'user2@mail.ru'])
msg2 = ('Подписка', 'Ваша подписка подтверждена',
        'subscripe@mail.ru',
        ['other_user@mail.ru'])

# Отправка писем зарегистрированным пользователям:

from django.contrib.auth.models import User
user = User.objects.get(username='admin')
user.email_user('Подъем!', 'Admin, не спи!', fail_silently=True)