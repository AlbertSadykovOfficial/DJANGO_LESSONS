"""
 Формирование ответа

 Основная задача контроллера - выдать ответ по запросу. (Обычно web-страница)

    Низкий уровень:
        HttpResponse([<содержимое>][,][content_type=None][,][status=200][,][reason=None])
                       содержимое == строка
                       content_type == MIME-тип
                       status       == код-ответа (200)
                       reason       == строковый статус ('OK')

        Класс ответа имеет атрибуты:
            content - содержимое ответа в типе byte.
            charset - кодировка
            status_code-код статуса
            ...
        И методы:
            write(<строка>) - добавляет сроку в ответ
            writelines(<последовательность строк>)
            flush() - принудительно переносит содержимое буфера записи в ответ
            has_header(<заголовок>)- проверка наличия заголовка
            setdefault(<заголовок>, <значение>) - создает в ответе заголовок с указанным значением.

        Класс поддерэивает ункциональность словарей:
            response['pragma'] = 'no-cache'
            age = response['Age']
            del response['Age']
"""
# Код контроллера, использующего никзоуровневые средства для создания овета:

    def index(request):
        resp = HttpResponse("Здесь Будет",
                            content_type='text/plain; charset=utf-8')
        resp.write(' главная')
        resp.writelines((' страница', ' сайта'))
        resp['keywords'] = 'Python, Django'
        return resp

"""
     Формирование ответа на основе шаблона:
     django.template.loader
     
         get_template(<путь к шаблону>) - загружает шблон с указанным путем, возвращает экз. Template
         select_template(<последовательность путей шаблонов>) - пытается загрузить шаблон по очередному пути
        
         Для получения обычной веб-страницы нудно объединить шаблон с данными - выполнить рендеринг.:
        
            render([context=<контекст данных>][,][requst=<запрос>]) - Метод класса Template

"""
from .models import Poster, Rubric
from django.template.loader import get_template

def index(request):
    poster = Poster.objects.all()
    rubrics = Rubric.objects.all()
    context = {'poster': poster, 'rubrics': rubrics}
    template = get_template('board/index.html')
    return HttpResponse(template.render(context=context,request=request))
#   return HttpResponse(template.render(context,request))

"""
        Загрузить шаблон с указанным путем.:
    
            render_to_string(<путь к шаблону>[, context=<контекст данных>][, requst=<запрос>])
            
            return HttpResponse(render_to_string('board/index.html', context, request))
"""

"""
    
    Класс TemplateResponse отложенный рендеринг шаблона:
    (Альтернатива HttpResponse)
    django.template.response
    
    Преимущества имеет при использовании посредников. 
    Отложенный ренеринг выполняется после прохождения всей цепочки зарегестрированных в проекте посредников.
    
    + В виде TemplateResponse генерируют ответы все высокоуровневые контроллер-классы
    
    TemplateResponse(<запрос>, <путь к шаблону>[, context=None][, content_type=None][, status=200])
            Запрос = Экземпляр класса HttpRequest
            template_name - путь к шаблону
            context_data - контекст шаблона
            
"""
from django.template.response import TemplateResponse

def index(request):
    poster = Poster.ojects.all()
    rubrics = Rubric.objects.all()
    context = {'poster':poster, 'rubric':rubrics}
    return TemplateResponse(request, 'board/index.html', context=context)



