# ФАЙЛ перенаправлений
from django.urls import path

from . import views
from .views import PosterIndexView
from .views import by_rubric # Во view.py
from .views import PosterCreateForm
from .views import PosterEditView
from .views import PosterDeleteView
from .views import PosterDetailView
from .views import PosterByRubricView

"""
    path(<шаблонный путь>, <контроллер>|<вложенный список маршрутов>[,<до параметры>][, name=<имя маршрута>])
    <шаблонный путь> может иметь слежующий вид: 
        < [<формат>:]<имя URL-ПАРАМЕТРА> >
            Форматы:
                str - любая непустая строка, не вкл слеши
                int - положительное целое чилсо, включая 0
                slug- строковый флаг (лат. буквы, цифры, знаки дефиса и подеркивания)
                uuid- уникальный универсаьный идентификатор
                path- непустая строка
   
   Передать данные в контроллер можно и объявив словарь python:
        vals = {'mode': 'index'} # передаем контроллеру-функции значение mode 
        urlpatterns = [
            path('<int:rubric_id>/', by_rubric, vals)
        ]
        
        def by_rubric(request,rubric_id,mode)
           ...
        
        Тогда в шаблоне можно использовть:
            <a href="{% url 'by_rubric' rubric_id=2 %}">...</a>
            
    
    
"""
# Прописываем пути к последующим файлам
#   Если это окончательный путь, вызываем функцию index() файла view
#   Если + есть постфикс folder, вызываем функцию folder() файла view
#   name - Имя маршрута <!-- Конструкция {% url '<name>' <postname>.pk %} - Шаблонизатор --->

urlpatterns = [
    #path('', PosterIndexView.as_view(), name='index'),
    path('delete_poster/<int:pk>/', PosterDeleteView.as_view(), name='delete_poster'),
    path('edit/<int:pk>/', PosterEditView.as_view(), name='edit'),
    path('detail/<int:pk>/', PosterDetailView.as_view(), name='detail'),
    path('add/', PosterCreateForm.as_view(), name='add'),
    path('<int:rubric_id>/', PosterByRubricView.as_view(), name='by_rubric'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'), # Вместо GET параметра <>-URL параметр
    path('', views.index, name='index'),
    path('folder/', views.folder, name='folder'),
    path('Poster_page/', views.html_temp1, name='Poster'),
    path('Poster_page/', views.html_temp2, name='Poster2')
]