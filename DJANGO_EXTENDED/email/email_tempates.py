"""

    Формирование писем на основе шаблонов:

        Письма можо формировать на основе шаблонов Django


"""

# Отпарвка письма на основе шаблона email/letter.txt
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
context = {'user': 'Александр Пушкин'}
s = render_to_string('email/letter.txt', context)
em = EmailMessage(subject='Оповещение',
                  body=s,
                  to=['apushkin@othersite.ru'])
em.send()