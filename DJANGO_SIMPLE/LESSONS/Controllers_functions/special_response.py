"""
    Специальные ответы

 Потоковый ответ
    Обычный ответ HttpResponse сначала сразу формируется в Оперативной Памяти, потом отправляется клиенту.
    Для отправки страниц большого объема HttpResponse не пригоден, следует исп ПОТОКОВЫЙ ОТВЕТ, который
    формируется и посылвется по частям.

    Класс потокового ответа: StreamingHttpResponse (в django.http)

        StreamingHttpResponse(<содержимое>[, content_type=None][, status=200][,reason=None])
            <Содержимое> задается в виде последовательность строк или итератора, на каждом проходе
            возвращающего строку. Остальные параметры как у HttpResponse

        Атрибуты:
            streaming_content - итератор, на каждом проходе возвращающий фрагмент содержимого ответа в виде объеута byte
            reason_phrase - цеочисленный код статуса
            streaming - True: потоковый ответ, False: нет

"""
from django.http import StreamingHttpResponse
# Пример отправки потокового ответа:

def index(request):
    resp_content = ('Здесь будет', ' главная', ' страница', ' сайта')
    resp = StreamingHttpResponse(resp_content, content_type='text/plain; charset=utf-8')
    resp['keywords'] = 'Python, Django'
    return resp


"""
 Отправка файлов
 
    Для отправки клиенту файлов применят FileResponse произодный от StreamingHttpResponse

        FileResponse(<файловый объект>
                    [, as_attachment=False][, filename=''][, content_type=None][, status=200][,reason=None])
        
"""
# Пример отправки файла (откроется в web-обозревателе)
from django.http import FileResponse

filename = r'c:/images/image.png'
#return FileResponse(open(filename,'rb'))

# Пример отправки файла (сохранится на локальном диске):
# Нужно в вызове конструктора указать:
#   as_attachment = True

filename = r'c:/images/archive.png'
#return FileResponse(open(filename,'rb'), as_attachment = True)

"""
 Отправка данных в формате JSON
 
    Класс JsonResponse 
        
        JsonResponse(<данные>[, safe=True][, encoder=DjangoJSONEncoder])
            <данные> должны быть в виде словаря Python
            safe - False: отправяем что-то отличное от словаря
            encoder - кодировщик в формат JSON
"""

data = {'title': 'Мотоцикл', 'content': 'Старый', 'price': 10000.0}
# return JsonResponse(data)