"""

    Авторизация

        Авторизация - выдача информации в соответствии с привелегиями, группами и т.д.
            В контроллерах
            В шаблонах

        (Весь код должен быть во view.py)

"""
"""
    Авторизация в контроллерах
        
        1) Надо закрыть от нежелательных посиителей контроллеры, выводящие на экран страницы

        redirect_to_login(<адрес перенаправления>[,
                          redirect_field_name='next'][,
                          login_url=None])
            redirect_field_name - имя GET-параметра (по умолчанию next)
            login_url - интернет-адрес страницы входа (по умолчанию в параметре LOGIN_URL)
            
"""

# Императивный подход (что делать, если не выполнен вход или нет прав)
from django.http import HttpResponseForbidden

def rubrics(request):
    if request.user.is_authenticated:
        # Все ок..
    else:
        return HttpResponseForbidden('Вы не имеете допуска к списку рубрик')
# или   return redirect('login')
# или   return redirect_to_login(reverse('board:rubrics'))

# Декларативный подход (говорим, что хотим допустить к какой-либо странице только пользователей,
#                      удовлетворяющим особым критериям)
"""
    # Допуск только авторизованных пользователей, иначе перенаправление на login_url (LOGIN_URL)
    login_required([redirect_field_name='next'][,][login_url=None])

"""
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

# Допустить к странице пользователей, выполнивших вход
@login_required
def rubrics(request):
#...

@login_required(login_url='/login/')
def rubrics(request):
# ...

"""

    # Допуск Авторизованных и прошедших проверку функцией:
    user_passes_test(<проверочная функция>[, redirect_field_name='next'][,login_url=None])

"""
@user_passes_test(lambda user: user.is_staff)
def rubrics(request):
# ...

"""

    # Допуск к странице пользователей имеющих заанные права:
    permission_required(<права>[, raise_exception=False][,login_url=None])

        raise_exception = True - возбуждать исключение, а не перенаправление
                                (тем самым, выводя страницу 403).
                                Если сообщение стоит выводить для пользователей,
                                выполнивих вход, но не имеющих необходимых прав,
                                следует спользовать этот декортатор с декортатором:
                                @login_required


"""

@permission_required('board.view_rubric')
def rubrics(request):
# ...

@permission_required('board.add_rubrics', 'board.change_rubric', 'board.delete_rubric')
def rubrics(request):
# ...


"""

    Декларативная авторизация в контроллерах-классах

        Реализуется посредством 3х классов примесей модуля django.contrib.auth.mixins:
            LoginRequiredMixin - для пользователей, выполнивших вход
            UserPassesTestMixin - выполнен вход + переопределен метод test_func
            PermissionRequiredMixin - для пользователей, имеющих заданные права

        Все эти классы производные от класса AccessMixin
        Класс AccessMixin поддерживает ряд атрибутов и методов:
            login_url -
            get_login_url() - возвращает значение login_url или LOGIN_URL
            permission_denied_message - хранит строковое сообщение о возникшей ошибке
            get_permission_denied_message() - получить сообщение об ошибке
            redirect_field_name -
            get_redirect_field_name
            raise_exception - Выдает 403, если недостаточно прав
            has_no_permission() - вызывается, если пользвоатель не выполнил вход или не имеет необх прав.
"""
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
# LoginRequiredMixin

# Разрешить добавлять новые объявления тольок тем, кто вошел на сайт
class PosterCreateForm(LoginRequiredMixin, CreateView):
    # ...

# Разрешить добавлять новые объявления тольок тем, кто вошел на сайт
class PosterCreateForm(UserPassesTestMixin, CreateView):
    # ...
    def test_func(self):
        return self.request.user.is_staff

# Разрешить добавлять новые объявления тольок тем, кто вошел на сайт
class PosterCreateForm(PermissionRequiredMixin, CreateView):
    permission_required = ('board:add_poster', 'board:change_poster', 'board:delete_poster')
    # ...


"""
    
    Авторизация в шаблонах:
        
        Если в числе активных обработчиков имеется:
            django.contrib.auth.context_proccessors.auth
        ,то он будет добавлять в контекст шаблона переменные:
            user и perms
        ,хранящие пользвателя и права
        
        Пример переменнй user:
        
            {% if user.is_authenticated %}
                ...
            {% endif %}
        
        Пример использования особого оъекта - perms:
            
            {% if 'board:add_poster' in perms %}
                ...
            {% endif %}
            
            {% if perms.board.add_poster %}
                ...
            {% endif %}
"""