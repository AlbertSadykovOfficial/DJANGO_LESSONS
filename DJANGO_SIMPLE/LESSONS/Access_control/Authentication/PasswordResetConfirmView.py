"""
        Контроллер PasswordResetConfirmView (Сброс пароля)
            (Наследуется от FormView)

        Запускается при переходе по интернет адресу, отправленному в письме с сообщением о сбросе пароля
        С параметром uid64 он получает закодированный ключ пользователя

        Получив GET-запрос, выводит страницу с формой для задания нвого пароля

        Атрибуты:
            template_name - путь к шаблону страницы (По умол: registration/password_reset_form.html)
            post_reset_login - Если True, пользователь после ввода пароля автоматически войжет на сайт
            success_url - Адрес на который нуно выполнить перенаправление после отправки письма
            extra_context - доп содержимое контекста шаблона (словарь)
            form_class - ссылка на класс формы для ввода адреса
                        (по умолчанию класс SetPasswordForm из django.contrib.auth.forms)
            token_generator - экз класса, выполняющего формирование жетона, котоырй включен в адрес
                              ведущи на страницу собственно сброса пароля
                              (по умолчанию класс PasswordResetTokenGenerator из django.contrib.auth.tokens)


"""
from django.contrib.auth.views import PasswordResetConfirmView

urlpatterns = [
    # ...
    path('accounts/reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='registration/confirm_password.html'),
             name='password_reset_confirm'),
]