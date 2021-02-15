"""
        Контроллер LoginOut (выход с сайта)
            (Наследуется от TemplateView)

        При получении GET запроса выполняется выход с сайта,
        затем идет перенаправление по адресу, указанном в next или next_page

        Атрибуты:
            next_page - адрес перенаправления (по умолчанию None)
            template_name - путь к шаблону страницы
            redirect_field_name - Имя GET-параметра из которого будет извлекаться адрес для перенаправления в виде строки
            extra_context - доп содержимое контекста шаблона (словарь)
            success_url_allowed - Множество, задающее хосты на которые нуно выполнить перенаправление

        В контексте шаблона создается переменная title, где хранится сообщение об успешном выходе

"""

# Дальнейший код должен быть в urls.py
# Страница входа в шаблоне: registration/logged_out.html
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #...
    path('accounts/logout/', LogoutView.as_view(next_page='board:index'), name='logout')
]

# Можно не прописывать адрес редиректа в контроллере, можно указать его в настройках сайта settings.py:
LOGOUT_REDIRECT_URL = 'board:index'