"""

    Агреатные вычисления - вычисления для всех записей в модели для определенного поля.

 Вычисления по всем записям модели:

    aggregate(<агрегатная функция 1>, ...,<>) # Вернет словарь

    # 1й вариант (позиционный параметр)
    Poster.objects.aggregate(Min('price')) # {'price__min': 10}
    # 2й вариант (именованный параметр)
    Poster.objects.aggregate(max_price = Max('price')) # {'max_price': 100}

    result = Poster.objects.aggregate(diff = Max('price') - Min('price'))
    result['diff'] # 90


 Вычисления по группам записей:

    annotate(<агрегатная функция 1>, ...,<>) # Вернет новый набор записей

    # 1й вариант (позиционный параметр)
        for x in Rubric.objects.annotate(Count('poster'))
            print(x.name, x.poster__count, sep='')
    # 2й вариант (именованный параметр)
        for x in Rubric.objects.annotate(cnt=Count('poster'))
            print(x.name, x.cnt, sep='')

    # Минимальная цена в каждой рубрике:
        for x in Rubric.objects.annotate(min=Min('poster__price'))
            print(x.name,':  ' , x.min, sep='')

    # Минимальная цена в каждой рубрике (+ убрать рубрики, не содержащие объявлений)
    # (использовав именованный параметр, создается поле в наборе записей, мы можем выполнить фильтрацию по этому полю)
        for x in Rubric.objects.annotate(cnt=Count('poster'),
                                         min=Min('poster__price').filter(cnt__gt=0)
                                         )
            print(x.name,':  ' , x.min, sep='')


 Агрегатные функции
    Count - кол-во записей
    Sum   - сумма значений в поле
    Avg   - среднее арифметическое
    StdDev- Стандартное отклонение
    Variance- Дисперсия
"""