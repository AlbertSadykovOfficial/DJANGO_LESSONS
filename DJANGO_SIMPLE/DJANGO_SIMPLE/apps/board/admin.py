# ФАЙЛ привязки данных приложения к админке + ее редактирования
from django.contrib import admin
from .models import Poster
from .models import Rubric

# Класс нужен для вывода читаемой информации в админке
class PosterAdmin(admin.ModelAdmin):
        list_display = ('name', 'about', 'price', 'published', 'rubric') # Поля, которые должны выводиться
        list_display_links = ('name', 'about') # Поля, при нажатии на которые будешь проваливаться в редактирование
        search_fields = ('name', 'about') # Фильтрация

# admin.site.register(Car) - если без класса
admin.site.register(Poster, PosterAdmin)
admin.site.register(Rubric)
