"""
    Библиотека Python Social Auth (регистрация и вход через социальные сети)
        http://python-social-auth.readthedocs.io/

        pip install social-auth-app-django

        Преднастройка:
        1) Регистрируем приложение:
            INSTALLED_APPS = [
                # ...
                'social_django'
            ]
        2) Выполнить миграции
        3) Если используетя PostgreSQL, добавим в модуль settings.py:
            SOCIAL_AUTH_POSTGRES_JSONFIELD = True
        4) Добавить в список классов, реализующих аунт. и авториз. класс social_core.backend.vk.VKOAuth2:
            + ДОБАВИТЬ этот список в settings.py
            AUTHENTICATION_BACKENDS = (
                'social_core.backend.vk.VKOAuth2',
                'django.contrib.auth.backends.ModelBackend'
            )
        5) Добавить в список контекста для исп нами шаблонизатора классы:
            TEMPLATES [
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                        #...
                    'OPTIONS': {
                        'context_processors': [
                            #...
                            'social_django.context_processors.backends',
                            'social_django.context_processors.login_redirect',
                        ],
                        #...
                    },
                },
            ]

        6) Доабвим в модуль settings.py параметры, указывающие полученные OD приложения и ключ
            SOCAIL_AUTH_VK_OAUTH2_KEY = 'XXXXXXX'
            SOCAIL_AUTH_VK_OAUTH2_SECRET = 'XXXXXXXXXXXXXXX'

        7) Если помимо всех данных, требуется получить еще и email, то в settings.py добавляют:
            SOCAIL_AUTH_VK_OAUTH2_SCOPE = ['email']

"""

"""

    Использование
    
        1) Создаем маршруты, ведущие на контроллеры, выполняющие регистрацию и вход:
            urlpatterns = [
                # ...
                path('social/', include('social_django.urls', namespace='social')),
            ]
            
        2) Добавляем в шаблон страницы входа гиперссылку, которая укажет на контроллер,
           выполняющий вход на сайт и регистрацию на основе сведений от VK
           
           <a href="{% url 'social:begin', 'vk-oauth2' %}">Войти через ВКонтакте</a>
           
           После успешного входа, будет произведен переход на страницу, указанную в параметре:
            LOGIN_REDIRECT_URL настроек проекта
"""