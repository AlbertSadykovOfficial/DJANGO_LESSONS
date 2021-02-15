"""

 Выборка всех записей.
    Все модели имеют атрибут objects, который позволяет манипулировать всеми записями в модели.
    Метод all() - возвращает набор всез записей модеои в виде QuerySet

 Извлечение одной записи:
    b = Poster.objects.first()  # Вернет 1ю запись
    b = Poster.objects.last()   # Вернет последнюю запись
    b = Poster.objects.earliest([<имя_поля 1> ,..., <<имя_поля n>]) # Вернет самую раннюю запись
    b = Poster.objects.latest([<имя_поля 1> ,..., <<имя_поля n>])   # Самое позднее

    Все методы поддреживаются классами Manager, RelatedManager и QuerySet - их можно вызывать у связных записей
    b1 = Poster.objects.filter(price__gte = 10000).first()
    r = Rubric.objects.get(name='Транспорт')
    b2 = r.poster_set.earliest('published')

 Получение количества записей в наборе (exists, count):
    r = Rubric.objects.get(name='Сантехника')
    Poster.objects.filter(rubric=r).exists() # False
    Poster.objects.count # Кол-во объявлений

 Поиск записи (get):
    r = Rubric.objects.get(name='Растения')
    r.pk # Запись, представляющая рубрику Растения

    r = Rubric.objects.get(pk=5)
    r # <Rubric: Название_Рубрики>

    r = Rubric.objects.get(pk=5, name='Сантехника')

    Если в моели есть хоть одно поле DateField или DateTimeField,
    то модель получает поддержку доп методов:
        get_next_by_<имя поля>([<условие поиска>])
        get_previous_by_<имя поля>([<условие поиска>])

    b.get_next_by_published()
    b.title

    Если мы имеем дело со 2й моделью и было задано произвольное переупорядочивание
    записей (казан параметрв order_with_respect_to), вторичная модель приобретает методы:
        get_next_in_order()
        get_previous_in_order()

    r = Rubric.objects.get(name='Мебель')
    b2 = r.poster_set.get(pk=34)    # pk = 34
    b1 = b2.get_previous_in_order() # pk = 37
    b3 = b2.get_next_in_order()     # pk = 33

 Фильрация:
    Poster.objects.filter(price__gte=10000) # Вернуть по условию
    Poster.objects.exclude(price__gte=10000)# Не возвращать по условию

    Написание условий фильтра:
        exact - Точне совпадение
        iexact - СОвдпаедние без учета регистра
        date - значение дата
        gt - больше
        lt - меньше
        ...

 Фильрация по значениям поей связных записей:
    Фильтрация 2-й модели по значениям 1й
    for x in Poster.objects.filter(rubric__name='Транспорт')

    Фильтрация 1-й модели по значениям 2й
    for x in Poster.objects.filter(poster__price__gt=10000)
        Можно указать дргугой фильтр, который будет применяться вместо имени 2й модели:
            rubric = models.ForeignKey(Rubric, on_delete=...., related_query_name='entry')
            -Тогда:
                for x in Poster.objects.filter(entry__price__gt=10000)

 Сравнение со значениями других полей
    ac = Another_Class('price')
    for x in Poster.objects.filter(content__icontains=f)

 Сложные условия фильтрации
    Для объединения фильраций понадобится класс Q из модуля django.db.models:
    q = Q(rubric__name='Недвижимость')|
        Q(rubric__name='Бытовая техника') &~
        Q(rubric__name='Транспорт')
    for x in Poster.objects.filter(q)

 Вывод уникальны записей:
    for x in Rubric.objects.filter(poster__price__gt=10000).distinct()

 Выбор указанного кол-ва записей:
    Rubric.objects.all()[:3]
    Rubric.objects.all()[5:]
    Rubric.objects.all()[2:8]
"""