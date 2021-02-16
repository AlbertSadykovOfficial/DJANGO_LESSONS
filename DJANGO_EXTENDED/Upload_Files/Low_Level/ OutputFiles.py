"""
    Вывод выгруженных файлов низкоуровневыми средствами

        Если выгруженные файлы не сохраняются в моделях,
        задача по и выводу несколько усложняется.

        Чтобы вывести все файлы в каталоге поможет функция scandir() модуля os

"""

# Вывод списка выгруженных файлов:
from django.shortcuts import render
from samplesite.settings import BASE_DIR
import os

FILES_ROOT = os.path.join(BASE_DIR, 'files')

# В шаблоне testapp/index.html нужно вывести изображения, хранящиеся в выгруженных файлах.
def index(request):
    imgs = []
    for entry in os.scandir(FILES_ROOT):
        imgs.append(os.path.basename(entry))
    context = {'imgs', imgs}
    return render(request, 'testapp/index.html', context)


# Контроллер, отправляющий выгруженный файл клиенту

from django.http import FileResponse

def get(request, filename):
    fn = os.path.join(FILES_ROOT, filename)
    return FileResponse(open(fn, 'rb'),
                        content_type='application/octet-stream'
                        )

# Маршурт, ведущий к контроллеру:
path('get/<path:filename>', get, name='get'),

