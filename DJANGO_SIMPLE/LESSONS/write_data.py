""" Запись данных
    from board.models import Poster
    from board.models import Rubric

 Правка данных:
    b = Poster.objects.get(pk=17)
    b.title = 'New title'
    b.save()

 Удаление записи:
    b.delete() # (1,{'board.Poster':1}) Кол-во удаленных записей и кортеж {'Модель':кол-во удаленных записей }

 Создание записей:
    1й вариант
        r = Rubric()
        r.name = 'Бытовая техника'
        r.save()

    2й вариант
        r = Rubric(name = 'Бытовая техника')
        r.save()

    3й вариант (автосохранение):
        r = Rubric.objects.create(name = 'Бытовая техника')

        Еще методы:
        get_or_create(<набор фильтров>[, defaults=None])
                     defaults - словарь с значениями для остальных полей создаваемой записи
            Пример:
            r = Rubric.objects.ger_or_create(name='Санехника')
            r # (<Rubric: Мебель>, False). True - найдена, False - создана

 Замечание о методе save()
    save([update_fields=None][,][force_insert=False][,][force_update=False])
        update_fields - если параметр указан, будут обновлены только соответствующие поля (а не вся таблица).
                        Выгодно, когда обнолвены часть от всех полей, особенно, когда имеются Большие текстовые
    Пример:
        b = Poster.objects.get(pk=17)
        b.title = 'Земельный участок'
        b.save(update_fields=['title'])

 Массовая запись данных (работают напрямую с БД, т.к. идут в обход программных инструментов)
    Допустим, в БД Объекта нужно внести корректировку для нескольких элементов, которые имеют определенное условие
    или удалить эти элементы, или просто внести многоэлеентов за раз.
    В это млучае поможет массовая запись данных с ее методами:

    bulk_create(<последовательность добавляемых записей>[, batch_size=None])
    Пример:
        r = Rubric.objects.get(name='Бытовая техника')
        Poster.objects.bulk_create([
                                    Poster(title='Пылесос', content='LG', price=2500, rubric=r),
                                    Poster(title='Стиралка',content='Bk', price=9500, rubric=r)
                                    ])

    update(<новые начения полей>)
    Пример:
        Poster.objects.filter(price=None).update(price=10)

    delete()
    Пример:
        Poster.objects.filter(content=None).delete()

 Валидация
    full_clean([exclude=None][,][validate_unique=True])
                exclude - Последовательность имен полей, значеня которых проверяться не будут
                validate_unique:
                    [True] - Если модель содержит уникальные поля, ьудет также проверяься уникальность
                             занесенных в них значений
                    [False]- Проверки проводиться не будут
    Метод не возвращает никакого результата, если данные некорректны он возбуждает исключение ValidationError
    Пример:
    b = Poster.objects.get(pk=1)
    b.full_clean() # Запись корректна, если сущствует

    b = Poster()
    b.full_clean() # Исключение, т.к новая модель пуста, а в ней есть обяательные поля, которые должны быть заполнены

ОБРАБОТКА СВЯЗНЫХ ДАННЫХ ?????
"""