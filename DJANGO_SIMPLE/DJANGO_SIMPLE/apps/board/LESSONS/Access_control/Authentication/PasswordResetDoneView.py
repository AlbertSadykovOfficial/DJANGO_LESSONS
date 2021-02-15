"""
        Контроллер PasswordResetDoneView (Уведомление об отправке письма для сброса пароля )
            (Наследуется от TemplateView)

        Атрибуты:
            template_name - путь к шаблону страницы
            extra_context - доп содержимое контекста шаблона (словарь)

        В контексте шаблона создается переменная title, где хранится сообщение об успешном выходе
"""
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    # ...
    path('accounts/password_reset/done/',
         PasswordResetView.as_view(
             template_name='registration/email_sent.html'),
         name='password_reset_done'),
]