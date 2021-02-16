"""
    Хранение файлов в моделях
        (django.db.models)

        Типы полей модели для хранения файлов:

            1) FileField - файл любого типа. (путь к файлу относительно MEDIA_ROOT)
                Параметры:
                    max_length - максимальная длина заносимого в поле путьи
                    upload_to - папка, куда будет выгружен файл тносительно  MEDIA_ROOT

                В upload_to может быть переадана:
                Строка:
                    archive = models.FileField(upload_to='') # В MEDIA_ROOT
                    archive = models.FileField(upload_to='archives/')
                    archive = models.FileField(upload_to='archives/%Y/%m/%d/')
                Функция:
                    def get_timestamp_path(instance, filename):
                        return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])
                    #   ...
                    file = models.FileField(upload_to = get_timestamp_path)


            2) ImageField - графический файл (рекомендуется использовать с библиотекой Pillow)
                Параметры:
                    max_length - максимальная длина заносимого в поле путьи
                    upload_to - папка, куда будет выгружен файл тносительно  MEDIA_ROOT

"""
from django.db import models

# Модель с полем для хранения выгруженного файла (models.py)
class Img(models.Model):
    img = models.ImageField(verbose_name='Изображение',
                            upload_to=get_timestamp_path)
    desc = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Изобржение'
        verbose_name_plural = 'Изображения'

"""
        Поля, валидаторы и элементы управления форм, служащего для указания файлов.
            
            Помимо простых валидаторов, в полях FileField и ImageField поддерживаеются и след. валидаторы:
                FileExtensionValidator - входит ли расширение файла в список допустимых
                    FileExtensionValidator(allowed_extensions=<допустимые расширения>[,
                                            message=None][,
                                            code=None])
                        allowed_extensions - Последовательнсоь допустимых расширений
                        message - строка с сообщение об ошибке
                        code - код ошибки
                    
                validate_image_file_extension - только графические файлы.
                    
                Дополнтельно:
                missing - файл не был выгружен
                empty - 0 размер
                contradiction - либо выбрать файл для выгрузки, 
                                либо уст флажок удаления файла из поля, 
                                но не одновременно
                        
"""

# Пример формы для выгрузки файла (файл forms.py):
from django import forms
from django.core import validators

from .models import Img

class ImgForm(forms.ModelForm):
    img = forms.ImageField(label='Изображение',
                           validators=[validators.FileExtensionValidator(
                               allowed_extensions=('gif', 'jpg', 'png')
                           )],
                           error_messages={'invalid_extension':'Этот формат файлов е поддерживается'}
                           )
    desc = forms.CharField(label='Описание',
                           widget=forms.widgets.Textarea()
                           )

    class Meta:
        model = Img
        fields = '__all__'



"""
    Обработка выгруженных файлов в контроллерах
    
        Но! :
            1) При выводе формы следует указывать:
                ectype='multipart/form-data'
             
            2) При повторном создании формы конструктору ее класса слеует передавать
            вторым позиционным параметром значение атрибута FILES объекта запроса.   

"""

# Сохранение картинки в моделе:
# Сохранение выпняет сама модль в папку MEDIA_ROOT
from django.shortcuts import render, redirect

from .models import Img
from .forms import ImgForms

def add(request):
    if request.method == 'POST':
        form = ImgForm(request.POST. request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testapp:index')
    else:
        form = ImgForm()
    context = {'form': form}
    return render(request, 'testapp/add.html', context)

"""
    Если для выгрузки файла используется форма, не связанная с моделью,
    нам понадобитсясамостоятельно занести выгруженный файл в нужное поле записи модели.
    
    (можно найти в атрибуте cleaned_data объекта формы)
"""
form = ImgNonModelForm(request.POST, request.FILES)
if form.is_valid():
    img = Img()
    img.img = form.cleaned_data['img']
    img.desc = form.cleaned_data['desc']
    img.save()

# Множественная загрузка файлов:
class ImgNonModelForm(forms.Form):
    img = forms.ImageField(#...
                            widget=forms.widgets.ClearableFileInput(attrs={'multiple': True})
    )

"""
    Вывод выгруженных файлов в шаблоне:
        
        Поле типа FieldFile, хранящее выгруженный файл, мы получим экз. класса FieldFile,
        представляющий разные сведения о выгруженном файле:
            url - адрес:
            name - путь к файлу, записанный относительно папки, в которую он загружен
            size - размер файла в байтах
            
        Для ImageField - экз. класса ImageFieldFile, производный от FieldFile,
        поддерживает 2 доп атрибута:
            width - ширина хранящегося в файле изображения в пискелях
            height - высота хранящегося в файле изображения в пискелях
        
        Пример:
            {% for img in imgs %}
                <div><img src="{{% img.img.url %}}"></div>
                <div><a href="{{% img.img.url %}}">Загрузить картинку</a></div>
            {% endfor %}
"""

"""
    Удаление выгруженного файла:
        
        При удалении моели файла, сам файл удаен не будет, его нужно удалять самостоятельно
        

"""

# Удалить файл с записью модели:
from django.shortcuts import redirect

def delete(request, pk):
    img = Img.objects.get(pk=pk)
    img.img.delete()
    img.delete()
    return redirect('testapp:index')

# Зачастую удобно реализвать удаление файлов в классе модели, переопределив метод delete()

class Img(models.Model):
    #...
    def delete(self, *args, *kwargs):
        self.img.delete(save=False)
        super().delete(*args, **kwargs)
