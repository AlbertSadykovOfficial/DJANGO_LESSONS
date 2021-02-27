"""

    Низкоуровневые инструменты

        Следует применять, если необходимо отправлять письма с вложениями

        Класс EmailMessage django.core.mail (обычное письмо)

         Конструктор принимает большое кол-во параметров, все они именованы и необязательны:
            subject - тема
            body - тело
            from_mail - адресотправителя в виде строки
            to - список или кортеж адресов получателей письма
            cc - список или кортеж адрсов получателей копии письма
            bcc - список или кортеж адрсов получателей скрытой копии письма
            reply_to - список или кортеж адрсов для отправки ответа на письмо
            attachment - список вложений, которые нужно добавить в письмо
                        Вложение моет быть задано в виде:
                            - Экз. класса MIMEBase из моделя email.mime.base или одного из его подклассов
                            - Кортежа их 3х элементов:
                                1) Строка имени файла
                                2) Строки ил объекта bytes с содержимым файла
                                3) Строки с MIME-типом

            headers - словарь с доп заголовками, которые нужно добавить в письмо
            connection - объект соединения, используемого для отправки письма
                        (Иначе будет установлено отдельное соединение)

        Методы:
            attach() - добавляет вложение к письму
                attach(<объект вложения>) (объект - MIMEBase)
                attach(<имя файла>, <содержимое файла>[, MIME-тип])

            attach_file(<путь к файлу>[, <MIME-тип>])  - добавляет файл в качетсве вложения.
            send([fail_silently=False]) - отправить письмо
            message() - Возвращается экз. класса SafeMIMEText
            recipients() - вернет список адресов всех получателей


        Класс EmailMultiAlternatives - письмо из нескольких частей
            (Наследует от EmailMessage)

            Добавляет поддержку метода

                attach_alternative(<сожержимое части>, <MIME-тип части>)

            Можно составить письмо из нескольких частей в разных форматах,
            обычно такое письмо содержит основную часть - Текст и вторую часть,
            которая написана с использованием HTML

"""

# Пример отправки часто встречающихся писем:
from django.core.mail import EmailMessage

# Отпарвка обычного письма
em = EmailMessage(subject='Test', body='Test', to=['user@supersite.ru'])
em.send()

# Оправка письма со вложением
em = EmailMessage(subject='Ваш новый пароль',
                  body='Новый пароль находится во вложении',
                  attachments=[('password.txt', '123456789', 'text/plain')],
                  to=['user@supersite.ru'])
em.send()

# Отпарвка письма с файлом
em = EmailMessage(subject='Запрошенный файл',
                  body='Получите запрошенный файл',
                  to=['user@supersite.ru'])
em.attach_file(r'C:\work\file.txt')
em.send()

# Пример письма из нескольких частей
from django.core.mail import EmailMultiAlternatives
em = EmailMultiAlternatives(subject='Test',
                            body='Test',
                            to=['user@supersite.ru']
                            )
em.create_alternatives('<h1>Test</h1>', 'text/html')
em.send()
