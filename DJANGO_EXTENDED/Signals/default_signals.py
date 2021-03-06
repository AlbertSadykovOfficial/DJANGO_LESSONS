"""

    Встроенные сигналы.

    Django имеет много встроенных сигналов, отправляемых различными подсистемами.

    Сигналы, отправляемые подсистемой доступа к БД:
    (модуль django.db.models.signals)

        pre_int - отправляется в самом начале создания записи модели (перед выполнением конструктора класса)
                 Параметры обработчика:
                    sender - класс модели, запись которой содается
                    args - сисок позиционных аргументов, переданных конструктору модели
                    kwargs - словарь именованных аргументов, переданных конструктору

                 Пример:
                    При создании нового объявления выполняем выражения:
                    Poster.objects.create(title='Дом', content='Двухэтажный', price=2093133)

                    Обработчик с параметром sender получит сслыку на класс Poster,
                    с параметром args - пустой список
                    с праметром kwargs-словаь {'title': 'Дом', 'content':'Двухэтажный', 'price': 2093133}

        post_init - отправляется в конце создания новой записи модели, после выполнения конструктора ее класса.
        pre_save - перед сохранением записи модели, перед save()
        post_save
        pre_delete - перед удалением записи
        post_delete
        m2m_changed - при изменении состава записей, связанных с обрабаываемой записью посредством связи "многие-со-многими"
            Пример:
            m = Machine.objects.create(name='Самосвал')
            s = Spare.objects.create(name='Болт')
            m.spares.add(s)
            s.machine_set.remove(m)
"""

# Пример вывода в консоли Django сообщения о добавлении объявления:
from django.db.models.signals import post_save

def post_save_dispatcher(sender, **kwargs):
    if kwargs['created']:
        print('Объявление в рубрике "%s" создано' % kwargs['instance'].rubric.name)

post_save.connect(post_save_dispatcher, sender=Poster)

"""
    
    Сигналы, отправляемые подсистемой обработки запросов и объявленные в моделу django.core.signals:
        request_started - оправляется в начале обработки запроса.
        request_finished
        get_request_exception - отправляется при возбуждении исключения в процессе обработки запроса

"""

"""

    Сигналы, отправляемые подсистемой разграничения доступа и объявленные в модуле django.contrib.auth.signals:
        user_logged_in - оправляется после выполненого входа
        user_logged_out
        user_logged_failed - отправляется если посетитель не смог войти на сайт

"""