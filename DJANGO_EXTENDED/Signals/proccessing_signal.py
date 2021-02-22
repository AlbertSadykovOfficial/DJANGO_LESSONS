"""

    Обработка сигналов

    Сигналы - экзепляры класса Signal и его производных,
    класс поддерживет 2 метода, предназначенные для:
        1) Привязки к сигналу обработчика
        2) Отмена привязки

    Код, выполняющий привязку обработчиков сигналов, которые должны действовать все время,
    записывается в модуле models.py, в котором объявляются классы моделей
    Если сигнал обрбатывается в течение какого-то определенного врепмени, его можно поместить
    в любой модель. Обычно их записывают в модуле views.py

    Привязка обработчика:
        connect(<обработчик>[, sender][, weak=True][, dispatch_uid=None])
            <обработчик> - функция или метод

            sender - класс из которого отправляется текущий сигнал (класс-отправитель)
                     (после чего обработчик будет обрабатывать сигналы именно от этого отправителя)

            weak - Если True, обработчик может быть удален из памяти при выгрузке модуля, в котором он объявлен.
                   Если False, обработчик никогда не будет выгружен ()

                   (!) Задавать этот параметр следует в том случае, если в качестве обработчика
                       выступает функция, вложенная в другую функцию, или метод объекта,
                       котоырй существует ограниченное время

            dispatch_uid - если к одному согналу привязывается ожин и тот же обработчик и необходимо
                           как-то идентифицировать их. В этих случаях указываются разные значения uid.

            (К одному и тому же сигналу может быть привязано произвольное кол-во обработчиков)

        Вместо метода connect() объекта, можн использовать декоратор receiver(<сигнал>) (django.dispatch)

        from django.dispatch import receiver
        @receiver(post_save)
        def post_save_dispatcher(sender, **kwargs):
         # ...

         Отменить привязку:
          disconnect([receiver=None][,][sender=None][,][dispatch_uid=None])
                receiver - обработчик, ранее привязанный к сигналу

          Пример:
          post_save.disconnect(receiver=post_save_dispatcher)
          post_save.disconnect(receiver=post_save_dispatcher, sender=Poster)
          post_save.disconnect(dispatch_uid='post_save_dispatcher_2')

"""

# Пример привязки обработчика к сигналу post_save, возникающему при сохранении записи модели:

from django.db.models.signals import post_save

# Привязка обаботчика post_save_dispatcher() к сигналу
post_save.connect(post_save_dispatcher)
# Привязка обработчика к сигналу, возникающему в модели Poster^
post_save.connect(post_save_dispatcher, sender=Poster)
# Двукратная привязка обрработчикаов к сигналу с укаанием разных значений параметра dispatch_id
post_save.connect(post_save_dispatcher,
                  dispatch_uid='post_save_dispatcher_1')
post_save.connect(post_save_dispatcher,
                  dispatch_uid='post_save_dispatcher_2')

"""

    Обработчик должен принимать как минимум один позиционный параметр, 
    с которым передается класс-отправитель сигнала.

"""


# Шаблон обработчика

def post_save_dispatcher(sender, **kwargs):
    # Тело функции оработчика
    # Получаем класс-отправтиеь сигнала
    snd = sender
    # Получаем значение переданного обработчику именованного параметра instance
    instance = kwargs['instance']
    # ...


class SomeClass:
    def post_save_dispatcher(self, sender, **kwargs):
# ...