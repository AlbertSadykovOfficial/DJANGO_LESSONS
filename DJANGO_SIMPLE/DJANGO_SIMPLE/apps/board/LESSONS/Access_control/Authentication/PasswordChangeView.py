"""
        Контроллер PasswordChangeView (Изменить пароль)
            (Наследуется от FormView)

        При получении GET запроса выводит на экран страницу с формой, где нужно вывести старый пароль и новый

        Атрибуты:
            template_name - путь к шаблону страницы
            success_url - Адрес на который нуно выполнить перенаправление после смены пароля
            extra_context - доп содержимое контекста шаблона (словарь)
            form_class - ссылка на класс формы для ввода нового пароля
                        (по умолчанию класс PasswordChangeForm из django.contrib.auth.forms)
"""
from django.contrib.auth.forms import PasswordChangeForm

urlpatterns = [
    #...
    path('accounts/password_change/',
         PasswordChangeForm.as_view(
             template_name='registration/change_password.html'),
             name='password_change'),
]

