"""

    Сигналы

        Сигнал - сущность, создаваемая Django при выполнении какого-либо дейстсвия
                (создание новой записи в модели, удаление записи, входе пользователя на сайт)

        К (сигналу)  можно привязать ОБРАБОТЧИК, котоырй будет вызываться при возникновении сигнала

        К примеру, приложение django-cleanup чтобы отслеить момент правки или удаления записи
        обрабатывает сигналы post_init, pre_save, post_save, post_delete

"""
