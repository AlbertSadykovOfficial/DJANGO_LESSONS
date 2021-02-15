"""
        Контроллер PasswordResetCompleteView (Уведомление об отправке письма для сброса пароля )
            (Наследуется от TemplateView)

        Атрибуты:
            template_name - путь к шаблону страницы (По умолчанию: registration/password_reset_complete.html)
            extra_context - доп содержимое контекста шаблона (словарь)

        В контексте шаблона создается переменная title, где хранится сообщение об успешном выходе
"""
from django.contrib.auth.views import PasswordResetCompleteView

urlpatterns = [
    # ...
    path('accounts/reset/done/',
         PasswordResetCompleteView.as_view(
            template_name='registration/password_confirmed.html'),
            name='password_reset_complete'),
]