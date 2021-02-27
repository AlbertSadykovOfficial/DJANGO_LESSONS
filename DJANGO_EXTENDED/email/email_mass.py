"""

    Массовая рассылка

        При отправке каждого отдельного письма
        экземпляр класса EmailMessage создает соединение с SMTP-сервером.
        Установление соединение - немалое время (пара секнуд),
        при массововй рассылке это неприемлимо.

        Параметр connection конструктора класса EmailMessage позволяет указать объект
        соединени, которое будет использовано для отправки текущего письма. Мы можем
        использовать одно и тоже соединение для отправки произовального кол-ва писем,
        устранив задержку на установление соединения.

        Получить соединение мы можем вызовом функции get_connection() из модуля:
        django.core.mail
        Функция в качесвте резельтата возвращает объект соединения.

"""

# Пример:
from django.core.mail import EmailMessage, get_connection

conn = get_connection()
conn.open()

email1 = EmailMessage(#...,
                      connection=conn)
email1.send()
email2 = EmailMessage(#...,
                      connection=conn)
email2.send()
email3 = EmailMessage(#...,
                      connection=conn)
email3.send()

# Или более удобно
email1 = EmailMessage() # Внури парамеметры
email2 = EmailMessage()
email3 = EmailMessage()
conn.send_messages([email1, email2, email3])
conn.close()