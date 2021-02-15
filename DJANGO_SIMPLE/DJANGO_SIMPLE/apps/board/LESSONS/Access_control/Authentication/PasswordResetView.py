"""
        Контроллер PasswordResetView (Отправка письма для сброса пароля)
            (Наследуется от FormView)

        При получении GET запроса выводит на экран страницу с формой, где нужно вывести старый пароль и новый

        Атрибуты:
            template_name - путь к шаблону страницы (По умол: registration/password_reset_form.html)
            subject_template_name - путь к шаблон темы электронного письма (По умол: registration/password_reset_subject.txt)
            email_template_name - путь к шаблону тела электронного письма в формате текста
            html_email_template_name - путь к шаблону тела электронного письма в формате HTML
            success_url - Адрес на который нуно выполнить перенаправление после отправки письма
            from_email - адрес электронной почты отправителя, который будет вставлен в отправляемое письмо
            extra_context - доп содержимое контекста шаблона (словарь)
            extra_email_context - доп содержимое контекста щшаблона для письма.
            form_class - ссылка на класс формы для ввода адреса
                        (по умолчанию класс PasswordResetForm из django.contrib.auth.forms)
"""
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    # ...
    path('accounts/password_reset/',
         PasswordResetView.as_view(
             template_name='registration/reset_password.html',
             subject_template_name='registration/reset_subject.txt',
             email_template_name='registration/reset_email.html'),
             name='password_reset'),
]


# Код шаблона registration/reset_subject.txt
{{ user.username }}: запрос на сброс пароля

# Код шаблона registration/reset_email.html

{% autoescape off %}
Уважаемый {{ user.username }}
Вы отправлили запрос на сброс пароля. Чтобы выполить сброс, пройдите
по этому адресу:
{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}

До свидания!
С уважением, администрация сайта
{% endautoescape %}