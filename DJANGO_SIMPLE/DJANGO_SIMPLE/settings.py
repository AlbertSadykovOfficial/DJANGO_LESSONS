import os
import sys
from pathlib import Path

# Запустить отладочный сервер:
# manage.py runserver

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Меняе папку приложений с коренного каталога в каталог apps
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# Секретный ключ для шифрования важных данных
# Может быть использован для атаки на сайт, поэтому е следует никому показывать
SECRET_KEY = '*wz891rd)46c_dcc73bog96^sxr4g_x(2l7+gj-ktps$i7sp2%'

# Редим работы сайта отладочный(true)/эксплуатационный(false)
DEBUG = True

ALLOWED_HOSTS = []


# Объявление используемых приложений (если что-то не используется, можно удалить)

INSTALLED_APPS = [
    'django.contrib.admin',         # Админка
    'django.contrib.auth',          # Разграничение доступа
    'django.contrib.contenttypes',  # Список всех моделей, объявленных во всех приложениях сайта
    'django.contrib.sessions',      # Хранение данных клиента на стороне сервера в сессиях
    'django.contrib.messages',      # Выводит всплывающие сообщения.
    'django.contrib.staticfiles',   # Обработка статических файлов
    'board.apps.BoardConfig',
]

# Списки посредников
# Посредник - программа, выполнящая предварительную обработку клиентского запроса перед передачей его контроллеру.
#             а так же окончательную обработку сгенерированную пконтроллером
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',            # Защита сайта от сетевых атак
    'django.contrib.sessions.middleware.SessionMiddleware',     # Работа сессий на низком уровне
    'django.middleware.common.CommonMiddleware',                # Предварительная обработка запросов
    'django.middleware.csrf.CsrfViewMiddleware',                # Защита от межсайтовых запросов при оработке данных
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Даобавляет атрибут идентификации пользователя
    'django.contrib.messages.middleware.MessageMiddleware',     # Обработка всалыващих сообщений на низком уровне
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   # Доп Защита сайта от сетевых атак
]

# Путь к модулю в котором прописаны маршруты уровня проекта
ROOT_URLCONF = 'DJANGO_SIMPLE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DJANGO_SIMPLE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#   ENGINE  - формат БД (SQLite, MySQL, PostgreSQL)
#   NAME    - путь к файлу БД
#   TIME_ZONE- временная зона ля назначения даты и времнив БД
#              (если БД не поддерживает хранение значений Даты и времени с указание временной зоны)
#   В случае серверных СУБД исполузуются и следующие параметры:
#       HOST - адрeс компа на котором СУБД
#       PORT - Номер TCP-порта, через который выполняется подключение к СУБД
#       USER - Имя от имени которого будет подключение к БД
#       PASSWORD
#       CONN_MAX_AGE - Время в течении котрого соеинение с БД будет открыто (в секундах),
#                      0 - соединение закрывается после обработки запроса
#       OPTIONS - Доп параметры для спеифичных СУБД (в виде словаря, элеметр указывает определенный параметр)
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Языковые настройки (их много, это лишь малая часть)
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True # Автоматический перевод на язык, указанный в параметре LANGUAGE_CODE

USE_L10N = True # Числа, дата и время будут при выводе будут формироваться по правилам языка LANGUAGE_CODE

USE_TZ = True # Хранить значения даты и времени по зоне TIME_ZONE


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
