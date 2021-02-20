"""

    Порядок выполнения посредников:

        Посрденики при получении запрса и формировании ответа выполняются дважды:
            1) При получении запроса (до того как запрос достигнет контроллера)
               (выполняются в том порядке, в котором записаны в MIDDLEWARE)
            2) После того как контроллер сгенерирует ответ (но до того как он отправтся к клиенту)
                Если ответ - экз. класса TemplateResponse, посредники выполняютсядо непосредсвенного
                рендеринга шаблона (что позволяет добавлять данные в контектс шаблона).
                (выполняются в ОБРАТНОМ порядке MIDDLEWARE)

"""

# Посреднкии зарегистрированные во вновь созданном проекте (settings.py)

# 1) При получении запроса выполнение пойдет сверху вниз
# 2) После чего управление будет передано контроллеру
# 3) После того, как контроллер сгенерируе ответ, все пойдет снизу вверх
# 4) После выполнения 1го посредника, ответ отпрвится клиенту
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ...
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]