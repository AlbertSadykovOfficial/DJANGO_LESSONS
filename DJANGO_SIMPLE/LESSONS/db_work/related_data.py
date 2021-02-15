""""
Выборка Данных (Извлечение, фильтрация, оперирование)

 Доступ к связным записям (Т.е. Поиск объединений и т.д.):
    ОДИН СО МНОГИМИ:
        Из 2й модели:
        b.rubric        # <Rubric: Недвижимость>
        b.rubric.name   # 'Недвижимость'

       Из 1й модели:
       +В классе 1-ой модели создается атрибут с именем <имя связной 2-ой модели>_set, который хранит Дисп. Обр. Связи
        Диспетчер обратной связи манипулирует с записями, СВЯЗАННЫМИ с текущей записью первичной модели
           +Можно изменить имя атрибута 1-й модели на свое, следует в конструкторе указать его как related_name:
                rubric = models.ForeignKey(Rubric, on_delete=...., related_name='entries')
                -Тогда доступ к диспетчеру обратной связи осуществляется таким образом:
                    for x in r.entries.all():
                        ...

        Пример:
        from Poster.models import Rubric
        r = Rubric.objects.get(name='Недвижимость')
        for x in r.poster_set.all():
            print(x.title)

        for x in r.poster_set.filter(price__lte=10000):
            print(x.title)

    ОДИН С ОДНИМ:
        Из 2й модели:
            au = AdvUser.objects.first()
            au.user             # <User: admin>
            au.user.username    # 'admin'
        Из 1й модели:
            u = User.objects.first()
            u.advuser # <AdvUser: AdvUser object (1)>

    МНОГИЕ СО МНОГИМИ:
        Из 2й модели:
            m = Machine.objects.get(pk=1)
            m.name # 'Самосвал'
            for s in m.spares.all():
                print(s.name) # Гайка Винт

        Из 1й модели:
            s = Spare.objects.get(name='Гайка')
            for m in s.machine_set.all():
                print(m.name) # Самосвал

"""