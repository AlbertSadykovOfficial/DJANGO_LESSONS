"""

    Влидация паролей

        Параметр AUTH_PASSWORD_VALIDATION настроек проекта,
        который задает набор валидаторов, применяемых для вальдации паролей
        При создании проекта в этот список заносятся  стандартных валидатора в сставе Django


    Стандартные валидаторы паролей

        Cтандартные валидаторы находятся в Модуле django.contrib.auth.password_validation:
            UserAttributeSimilarityValidator() - помогает проверить, что пароль достаточно отличается от других
                                                 сведений о пользователе:
                UserAttributeSimilarityValidator([user_attributes=self.DEFAULT_USER_ATTRIBUTES][,]
                                                  [max_similarity=0.7])

                user_attributes - задает последовательность имен полей модели User из которых будут браться сведения,
                                (имена в виде строк)
                                По умолчанию DEFAULT_USER_ATTRIBUTES, включающий username, first_name, last_name, email
                max_similarity - задает степень схожести пароля со значением из указанных в последовательносьть
                                 0 - будут отклоняться все пароли без исключений
                                 1 - будут отклоняться пароли, полностью совпадающие с значением полей

            MinimumLengthValidator([minimum_length=8]) - проверка на мнимальное кол-во символов

            CommonPasswordValidator([password_list_path=self.DEFAULT_PASSWORD_LIST_PATH])
                Проверяет не входит ли пароль в перечень наиболее часто встречющихся паролей
                password_list_path - полный путь к файлу .txt со списком недопустимых паролей

            NumericPasswordValidator - проверяет, не содержит ли пароль одни цифры


        Пример, задающий новый список валидаторов:
            AUTH_PASSWORD_VALIDATION = [
                {
                    'NAME': 'django.contrib.auth.password_validation.' + 'MinimumLengthValidator',
                    'OPTIONS': {'min_length': 10}
                },
                {
                    'NAME': 'django.contrib.auth.password_validation.' + 'NumericPasswordValidator',
                }
            ]
"""
"""

    Написание своих вылидаторов

        Должны быть реализованы в виде классов + объявлять 2 метода:
            validate(<проверяемый пароль>[, user=None]) - выполняет валидацию проверяемого пароля.
            get_help_text() - возвращает строку с требованиями к вводимому паролю
"""
from django.core.exceptions import ValidationError

class NoForbiddenCharsValidator:
    def __init__(self, forbidden_chars=(' ',)):
        self.forbidden_chars = forbidden_chars

    def validate(self, password, user=None):
        for fc in self.forbidden_chars:
            if fc in password:
                raise ValidationError(
                    'Пароль не должен содержать недопустимые символы %s'
                    % ', '.join(self.forbidden_chars),
                    code='forbidden_chars_present'
                )

    def get_help_text(self):
        return 'Паролль не должен содержать недопустимые символы %s' % ', '.join(self.forbidden_chars)

"""
    После этого стоит задать валидатор
    
        AUTH_PASSWORD_VALIDATION = [
            {
                'NAME': 'django.contrib.auth.password_validation.' + 'MinimumLengthValidator',
                'OPTIONS': {'forbidden_chars': ' ', ',', '.', ':', ';'}
            },
        ]
"""

"""
    Выполнение валидации паролей
    
        Функции из модуля django.contrib.auth.password_validation:
        
            validate_password(<пароль>[, user=None][, password_validators=None])
            
            password_validators_help_texts([password_validators=None])
                Возвращает список строк, содержащих требоваия к вводимым паролям
            
            password_validators_help_texts_html([password_validators=None])
                                                               
            password_changed(<пароль>[, user=None][, password_validators=None])
                Сообщает всем валидаторам, что пароль изменился
                
                !!! Вызов этой фукции следует осуществлять после каждой смены пароль, 
                    если для этого не использовалась функция set_password(),
                    в таком случае ф-ция password_changed вызывается автоматически
                    
            
            password_validators - список валидаторов, которые юудут заниматься валидацией пароля
                                  Если он не указан, используется список параметра AUTH_PASSWORD_VALIDATORS
            
            Чтобы сформировать свой список валидаторов, следует применить функцию:
                get_password_validators(<настройки валидаторов>)
            
        Пример:
        from django.contrib.auth import password_validation
        my_validators = [
            {
                'NAME': 'django.contrib.auth.password_validation' + 'NumericPasswordValidator',
            },
            {
                'NAME': ' NoForbiddenCharsValidator ',
                'OPTIONS': {'forbidden_chars': (' ', ',', '.', ':', ';')}
            }
        ]
        validator_config - password_validation.get_password_validators(my_validators)
        password_validation.validate_password(password, validator_config)
"""