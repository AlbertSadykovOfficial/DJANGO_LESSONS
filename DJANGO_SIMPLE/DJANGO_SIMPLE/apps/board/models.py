# ФАЙЛ, кторый отвечает за все Модели относящиеся к приложению в БД
from django.db import models


# Создать объект в консоли Django:
# car_1 = Poster(name='LADA_Granta', about='Гранта', price = '228000')
# Poster.objects.create(name='Mazda_RX7', about='Хана', price=1800000)

# При создании модели приложения:
# В БД создается таблица AppName_ModelName -> board_poster
#                        С автоматическим полем id (AUTOICREMENT) и указанными параметрами

# Параметры, поддерживаемые всеми моделями:
#    verbose_name - Название поля, которое будет выводиться на административной версии сайте
#    help_text    - Поясняющйи текст.
#    default      - Значение по умолчанию, если поле осталось пустым
#    unique       - Должно быть уникальное занчене в пределах таблицы, при попытке внести значение будет ислючение
#         unique_for_date - Уникальность  пределах даты
#         unique_for_month- Уникальность  пределах месяца
#         unique_for_year -Уникальность  пределах Года
#    null - необязательность к заполнению, если False в таблице должно раниться хоть какое-то значение
#    blank- необязательность к заполнению в поля в форме, даже при условии, что null = True
#    choice - полседовательность значений, доступных для занесение в поле (список)
#            KINDS= (('a','Куплю'),('b','Продам'))
#    db_index - создать по текущему полю индекс
#    primary_key - Сделать это поле ключевым (поле станет обяхательным к заполнению, неявно null=False, unique=Trur)
#    editable - Ввводить поле на экран в составе формы
#    db_column- Имя поля таблицы в виде строки, если не указно, будет как AppName_ModelName (но это не точно)

# Классы полей моделей:
#    AutoField - Автоинкрементное поле (32 разряда)
#    BigAutoField - Автоинкрементное поле (64 разряда)
#    ...
#    CharField - Строковое поле
#    ...
#    NullBooleanField - Возмоность хранить bool + null
#    BigIntegerField - 64-разрадяное int
#    DecimalField - вещественное число заданной точности DecemicalField(max_digits=8, decemical_places=2)
#    ...
#    DurationField - промежуток времени, предсатвленный объектом timedelta модуля python
#
# Связи между моделями "Один-со-многими"(ForeignKey) - Одна первичная модель, множество вторичных
#
#    ForeignKey(<связываемая первичная модель>,
#               on_delete=<поведение при удалении записи>
#               [,<остальные_параметры>])
#
#    На уровне БД поле внешнего ключа представляется полем таблицы с именем <имя поля внешнего ключа>_id
#
#    1й Параметр (Ссылка на модель):
#    Если код первичной модели (с которой связываемся) обявлен раньше, то ссылка - имя  : Rubric
#    Если код первичной модели (с которой связываемся) обявлен позже , то ссылка - текст: 'Rubric'
#    Если код первичной модели (с которой связываемся) в другом приложении, то ссылка: 'OtherApp.Rubric'
#    Если нужно создать модель, ссылающуюся на себя, то ссылка: 'self'
#
#    2й Параметр (Повдение при удалении записи первичной модели):
#    CASCADE - Удаление всех связных записей первичной модели
#    PROTECT - Предотвращение удаление с вызовом исключения
#    SET_NULL- Заносит в поле внешнего ключа всех связных записей вторичной модели null.
#    SET_DEFAULT - Заносит в поле внешнего ключа всех связных записей вторичной модели значение по умолчанию.
#    SET(<значение>) - Заносит в поле внешнего ключа указанное значение
#    DO_NOTHING - Ничего не делает.
#
#    Необязательные параметры:
#    limit_choices_to - вывести в списке связываемых записей первичные значения удовлетворяющие фильтрации
#    related_name - имя атрибута записи первичной модели, предназначенного для доступа к связным записям 2й модели
#    related_query_name - Имя фильтра, который будет применяться во вторичной модели
#                         для фильтрации по значениям из записи 1й модели
#    to_field -  имя поля первичной модели по которому будет выполнена связь в вие строки.
#    db_constraint - в таблице БД будет создана связь, позволяющая сохраняь ссылочную целостность.
#
# Связи между моделями "Один-с-одним"(OneToOneField) Одна первичная модель, одна вторичная
#    (К примеру: Связь модли AdvUser с доп сведениями о пользователе с модулью User)
#    OneToOneField(<связываемая первичная модель>,
#               on_delete=<поведение при удалении записи>
#               [,<остальные_параметры>])
#    1й Параметр (Ссылка на модель)
#    2й Параметр (Повдение при удалении записи первичной модели)
#
# Связи между моделями "многие-со-многими"(ManyToManyField) Много первичных моделей, много вторичных
#    Все модли равноправны, пожтому первичность и вторичность теряет смысл
#    Обявление следует делать только в 1 модели, но не в обеих сразу
#
#    ManyToManyField(<вторая связываемая модель>[,<остальные_параметры>])
#
#    На уровне БД для предсавлния связи такого типа создается таблица
#        <псевдоним приложения>_<имя класса ведущей модели>_<имя лкасса ведомой модели> (связующая таблица)
#    Таблица будет иметь ключевое поле id и по 1 полю на каждую из связываемых моделей с именем вида:
#        <имя класса связываемой модели>_id
#    1й Параметр (Ссылка на модель)
#    Дополнительные Параетры:
#    symmetrical - для связи модели самой с собой (симметричная связь)
#    through - Класс, представляющий связующую таблицу в виде ссылки на него, лиюо в виде имени, прелставл строкой.
#    through_fields - Исп в случае применения связующей модели в параметре through конструктора. (Кортеж)
#    db_table - имя связующей таблицы.(Если связующая модель не используется)
#
#
# Параметры самой моели объявляются в подклассе Meta
#
# У модели можно задать интерет-адрес (Императивным методом (переопределение) или Декларативным (через settings.py))
#
# Дополнительные методы модели
#    __str__() - возвращающий строковое представление класса
#    save()    - Сохранение записи (можем  пееропредлить и проверять в методе на како-то соответствие)
#    delete()  - Удаление записи
#    Можно объявлять ддоп поля, знаение котрого вычисляется по основе других данных и которое доступно только для чтения
#
#
# Валидация Модели
#    Валидаця - проверка данных, занеченных в поля модели на корректность.
#    Стандартные валидаторы (django.core.validators):
#          Вклюают функционал проверки на Длину введенных данных, регулярные выражения, email,
#          корректность URL, наличие \x00 символа, больше или меньше нужного значения наше число,
#          проверка на ip
#    Пример:
#         title = models.CharField(max_length=50, validators =[validators.RegexValidator(regex='^.{4,}$')])
#
#    Вывод собственных сообщений о ошибках
#    Пример:
#         title = models.CharField(max_length=50,
#                                  validators =[validators.RegexValidator(regex='^.{4,}$')]
#                                  error_messages={'invalid': 'Неправильное название товара'}
#                                  )
#     Коды ошибок:
#     null - невозможность зранения null
#     ...
#     invalid_choice - в поле списка внесено значение, не указанное в списке
#     ...
#     null_characters_not_allowed - сохраняемая строка содержит нулевые символы \x00
#
#    Свои валидаторы:
#         ValidationError(<описание ошибки>[,code=None][,params=None])
#         Для боле сложных проверок следует делать валидаторы как классы
#
#         Пример:
#         def validate_even(val):
#              if val % 2 != 0:
#                   raise ValidationError('Число %(value)s нечетное', code='odd',params={'value':val})
#
#    Валидация модели
#    Т.к Модели - это набор разных параметров,
#                 то Валидатор для них - набор (список) из исключений для всех этих параметров
#    Пример:
#         Class board(models.Model):
#             ...
#              def clean(self):
#                   errors = {}
#                   if not self.content:
#                        errors['content'] = ValidationError('Укажте описание товара')
#                   if self.price and self.price < 0:
#                        errors['price'] = ValidationError('Укажте неотрицательную цену')
#                   if errors:
#                        raise ValidationError(errors)
#    Чтобы узнать об ошибке относящейся к модели в целом, следует использовать
#    NON_FIELDS_ERRORS из пакета django.core.exceptions
#    errors[NON_FIELDS_ERRORS] = ValidationError('Ошибка в модели!')
#    v
class Poster(models.Model):
    name = models.CharField(max_length=20, verbose_name='Марка')
    about = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    # Класс описания, который позволет настроить отображение/представление объекта
    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    # Т.к. в модели 1 поле, то для вывода в Админку нормальной информации
    #    то лучше переопределить метод str, возвращающий строковое представление класса
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
