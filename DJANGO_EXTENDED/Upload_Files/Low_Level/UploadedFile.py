"""

    Класс UploadedFile - выгруженный файл (сохранение)

        Все выгруженые файлы хранятся в словаре FILE объекта запросаю
        Каждый из файлов представляет экземпляр UploadedFile

        атрибуты UploadedFile:
            name
            size
            content_type
            content_type_extra
            charset

        Методы:
            multiple_chunks([chunk_size=None]) - True, если файл настоолько велик, что
                                                для обработки его придется разбивать на разрные
                                                части
                                                False, елси он может быть обработан как единое целое
            read() - считывает и возвращает в качесте результата все содержимое файла.
            chunks([chunk_size=None]) - возвращает итератор,
                                        который на каждой иерации выдает очередную часть файла.
                chunk_size - размер отдельной части
                (Метод рекомендуется использовать для слишком больших файлов, чтобы быть обработанным
                за 1 раз, метод multiple_chunks возвращает True)

"""

# Сохранение выгруженного файла в папку files в папке проекта:
# Т.е сохранять файл мы можем в любой папке, а не тольок в тех, путь которых указан в MEDIA_ROOT

from django.shortcuts import render, redirect
from samplesite.settings import BASE_DIR
from datetime import datetime
import os

from .forms import ImgForm

FILES_ROOT = os.path.join(BASE_DIR, 'files')

def add(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['img']
            fn = '%s%s' % (datetime.now().timestamp(),
                           os.path.splitext(uploaded_file.name)[1]
                           )
            fn = os.path.join(FILES_ROOT, fn)
            with open(fn, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return redirect('testapp:index')
    else:
        form = ImgForm()
    context = {'form': form}
    return render(request, 'testapp/add.html', context)