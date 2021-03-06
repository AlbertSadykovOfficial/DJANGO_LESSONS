# Generated by Django 3.1.5 on 2021-01-20 14:15

from django.db import migrations, models


# Миграция - программный модуль, создающий в БД все необходимые  для модели структуры:
#            таблицы, поля, индексыЖ правила,связи
#
#   При выполнении миграции генериируется SQL код, выполняющий создание этих структур
#   Написание своих миграций: https://docs.djangoproject.com/en/2.1/ref/migration-operations/
#
# Формирование миграций:
#   manage.py makemigrations [<список псевдонимов приложений, резделенных проблами>]
#                            [--name|-n <имя миграции>] - имя формируемой миграции
#                            [--noinput] [--no-input]   - отключает вывод на экран сведений о миграции
#                            [--dry-run] - выводит сведения о формируемой миграции, но не формирует ее
#                            [--check]   - выводит сведения изменилась ли миграция с последнего раза
#                            [--merge]   - устранение конфликтов между миграциями
#                            [--empty]   - создает пустую миграцию для програмиирования ее вручную
#
#   Миграцию можно переименовать, только если ее ее не выполнены, если миграцию выполнили, то будет запись в БД
#
# Выполнение миграций:
# manage.py migrate [<псевдоним приложения> [<имя миграций>]]
#                   [--fake-initial] - Пропускает выполнение начальной миграции.
#                                      (Если в БД на момент 1го выполнения миграций
#                                       уже пристутсвуют все необходимые структуры)
#                   [--noinput] [--no-input] - отключает вывод на экран сведений о миграции
#                   [--fake] - помечает миграции как выполненные, но не вносит никаких изменений в БД.
#                              (Пригодиться, если все изменения в БД были внесены вручную)
#   На кадую выполненнуб миграцию в таблицу django_migrations БД добавляется тельная запись,
#   хранящая имя имя модуля миграции, имя приложения, дату и время выполнения
#
# Слияние миграций
#   Если в процессе изменения модели множество раз выполнялись миграции, то их можно
#   объединить в ОДНУ - провести слияние миграций.
#
#      manage.py squashmigrations <псевдоним приложения>
#                                 [<имя первой миграции>] <имя последней миграции>
#                                 [--squashed_name <имя результирующей миграции>] - (иначе будте по умолчанию)
#                                 [--no-optimize] - Отмена оптимизации кода миграций
#                                                   (может помочь, если слияние не удалось)
#                                 [--noinput] [--no-input] - отключает вывод на экран сведений о миграции
#   Пример:
#   manage.py squashmigrations board 0004 # Все миграции начиная с первой
#   manage.py squashmigrations board 0002 0004 # Диапазон миграций
#
# Вывод списка всех миграций:
#   manage.py showmigrations [<список псевдонимов приложений, разделенных пробелами>] - иначе выведет все
#                            [--plan] - вывести вместо списка план миграций (списко отсортировованных миграций)
#                            [-p]
#   [X]-Миграция выполнена
#   [ ]-Миграция не выполнена
#
# Отмена всех миграций (отдельную отменить невозможно)
#  manage.py migrate testapp zero

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('about', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]
