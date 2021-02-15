"""
        Контроллер LoginView (вход на сайт)
            (Наследуется от FormView)

"""

# Дальнейший код должен быть в urls.py
# Страница входа в шаблоне: registration/login.html
from django.contrib.auth.views import LoginView

urlpatterns = [
    #...
    path('accounts/login/', LoginView.as_view(), name='login')
]