from django.contrib import admin
from django.urls import path, include

# Можно изменить модуль маршрутов к приложениям с (urls.py) на другой в settings.py:
#    ROOT_URLCONFIG

# Путь в вид регулярных выражений:
# django.urls import re_path
#  re_path(<регулярное выражение>,
#          <контроллер>|<вложенный список маршрутов>[,
#          <доп параметры>][, name=<имя маршрута>]
#           )
# re_path(r'^add/$', index, name='index')

# Прописываем пути к последующим файлам
# Указываем, что при текущей сcылке следующим файлом будет board/urls.py
urlpatterns = [
    path('board/', include('board.urls')),
    path('admin/', admin.site.urls),
]
