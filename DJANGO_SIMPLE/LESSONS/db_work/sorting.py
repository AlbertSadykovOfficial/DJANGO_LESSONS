"""
Сортировка

    order_by([<имя поля 1>,...,<имя поля n>])

    По возрастанию
    for x in Rubric.objects.order_by('name')

    ПО убыванию (нужно предворить знаком(-))
    for x in Poster.objects.order_by('rubric__name','-price')

    Поменять сортировку на противоположную:
    for x in Rubric.objects.order_by('name').reverse()

    Каждый вызов метода обнуляет предыдущий, поэтому следующий пример не учтет 1й order_by:
    for x in Poster.objects.order_by('rubric__name').order_by('-price')
        Соответственно, чтобы отменить сортировку, следует сделать так:
        for x in Poster.objects.order_by()

    Выдать записи в случайном порядке (но это может отнять много времени):
    for x in Rubric.objects.order_by(?)


"""