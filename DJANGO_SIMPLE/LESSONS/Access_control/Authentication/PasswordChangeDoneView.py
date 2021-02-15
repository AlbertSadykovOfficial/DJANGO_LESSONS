"""
        Контроллер PasswordChangeDoneView (Уведомление об успешной смене пароля )
            (Наследуется от TemplateView)

        Атрибуты:
            template_name - путь к шаблону страницы
            extra_context - доп содержимое контекста шаблона (словарь)

        В контексте шаблона создается переменная title, где хранится сообщение об успешном выходе
"""
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    # ...
    path('accounts/password_change/done/',
         PasswordChangeDoneView.as_view(
             template_name='registration/password_changed.html'),
             name='password_change_done'),
]
