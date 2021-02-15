"""
    Контроллер - Перенаправление (django.views.generic.base -> RedirectView)
    (Наследует от View
     Выполняет перенаправение на указанный адрес)

     Атрибуты:
        url - адрес переадресовки, может включать спецификаторы, пожжерживаемые python (%),
                указываешь параметр,туда значение заносится
        pattern_name - задает имя именованного маршрута.
        query_string - True: все GET-параметры, присутствующее в текущем интернет-адресе,
                            будут добавлены к интрент адресу на который будет перенаправление.
        get_redirect_url(...) - возвращает строку с интрнет адресом, на который слежует выплнить перенаправление
        permanent - True: Будет выполнено постоянное перенаправление с кодом (301)
                    False:Будет выполнено временное перенаправление с кодом (302)

"""

# Пример:
# Перенаправление с /detail/<год>/<месяц>/<число>/<ключ>/
#                на /detail/<ключ>/

# Добавим в список маршруты:
# path('detail/<int:pk>/',PosterDetailView.as_view(), name='detail')
# path('detail/<int:year>/<int:month>/<int:day>/<int:pk>', PosterDetailView.as_view(), name='old_detail')

# Код контроллера:
from django.views.generic.base import RedirectView
class PosterDetailView(RedirectVeiw):
    url  = '/detail/%(pk)d/'