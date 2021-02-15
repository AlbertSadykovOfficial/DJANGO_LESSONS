"""
    Вычисляемые поля -

    Функциональные поля - поля, значение которых не берутся из БД, а вычисляются на основе каких-то данных,
                          они вычисляются на компьютере программой.
    Вычисляемые поля - вычисляются средсвтвами СУБД. Обычно не сложные вычисления (в пределах возможности SQL).


 Простейшие вычисляемые поля
    1) Вычисляемые поля создаются методом annotate().
    2) Константы int, float  указываются как есть
    3) Константы строки записываются через экземляр класса Value(<значение константы>[,output_field=None])
    4) Для вычислений применяются операторы +,-,*,/, //

    from x in Poster.objects.annotate(half_price=F('price')/2):
        print(x.half_price)

    from x in Poster.objects.annotate(full_name=Concat(F('title'),
                                                        Value(' ('),
                                                        F('rubric__name'),
                                                        Value(')')
                                                       )
                                        ):
        print(x.full_name) # Стиральная машина


 Функции СУБД:
    Представляются набором классов модуля (django.db.models.functions)

    Примеры классов:
    Coalesce(<значение 1>,...,<>)
        Значения предстваляются строками, экземплярами классов F, и Value
        Пример:
        Coalesce('content', 'addendum', Value('--пусто--')) # Если content != null, то венрнется addendum и тд...

    Least - возвращает наименьшее переданное ему значение
    Cast(<значение>, <тип>) - принудительно преобразыет значение к указанному типу
    Concat - объединяет значение в одну строчку.
    ...
    Replace(<значение>, <заменяемая подстрока>,[<заменяемая подстрока>])

 Условные выражения в СУБД

    Case(<условие 1>, <условие 2>, ..., <условие n> [, default=None][,output_field=None])
    When(<условие>, then=None) # Условие ожно записать как (Экземп. кл. Q)

    for x in Rubric.objects.annotate(cnt=Count('poster'),
                                     cnt_s=Case(When(cnt__gte=5, then=Value('Больше 4')),
                                                When(cnt__gte=3, then=Value('Меньше 4')),
                                                default=Value('РОВНО 4'),
                                                output_field=CharField()
                                                )):
        print('%s: %s' % (x.name, x.cnt_s))

 Вложенные запросы:

 Объединение наборов записей:

    union(<набор записей 1>, <набор записей 2>, ..., <набор записей n>)

    b1 = Poster.objects.filter(price_gte=10000).order_by()
    b2 = Poster.objects.filter(rubric__name='Бытовая Техника').order_by()
    for x in b1.union(b2):
        print(b.title, sep=' ')

    intersection(<набор записей 1>,...,<>) - вернет набор с пересечением записей
    difference(<набор записей 1>,...,<>) - вернет набор, содерж щаписи, которые имеются только в 1 из наборов

 Извлечение значений только из заданных полей (а не все целиком):

    values([<поле 1>, <поле 2>,... <поле n>]) # Верент набор записей QuerySet

    Пример:
    Poster.objects.values() # Вернет набор со всеми полями моели
    Poster.objects.values('title', 'price', 'rubric')
    Poster.objects.values('title', 'price', rubric_id=F('rubric'))

    values_list([<поле 1>, <поле 2>,... <поле n>],[flat=False],[named=False]) - то же, что и values(), но вернет кортежи

    flat - Если нужно значение 1го поля
    named - будут именованные картежи
    Пример:
    Poster.objects.values_list('id')            # [(2,),(3,),(22,),(12,),(55,),(23,)]
    Poster.objects.values_list('id', flat=True) # [2,3,22,12,55,23]

    dates(<имя поля>, <часть даты>[, order='ASC']) - Набор записй с уникальными значениями даты.
    datetimes(<имя поля>, <часть даты и времени>[, order='ASC'][,tzinfo=None]) - что и dates(), оно манипулирует значениями даты и времени
    in_bulk(<послеовательность значенйи>[,field_name='pk']) - Ищет в модели запись, чье имя задано параметром field_name,
                                                              хранит значние из указанной последовательности.
    Пример:
    Rubric.objects.in_bulk([1,2,3]) # {1: <Rubric: Недвижимость>, 2: <Rubric: Транспорт>, 3: <Rubric: Бытовая Техника>}
    Rubric.objects.in_bulk(['Транспорт', 'Мебель'], field_name='name') {'Мебель': <Rubric: Мебель>, 'Транспорт': <Rubric: Транспорт>}

 Получение значений из полей со списом

    b = Poster.objects.get(pk=1)
    b.get_kind_display() # ПРОДАМ
"""