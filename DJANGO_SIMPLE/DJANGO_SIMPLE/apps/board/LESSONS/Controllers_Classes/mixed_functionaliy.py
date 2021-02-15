"""
    Контроллеры-классы смешаннй функциональности
    (Рекомендуется избегать, лучше барть за основу контроллеры низкого уровня и реализововать логику самостоятельно)
    Большая часть функциональность контроллеров наследуется от классов-примесей.
    Поэтому, если брать нудные нам примеси, мы можем создавать контроллеры смешанной функциональности.

    К примеру, нам нужно вывести сведения о выбранной записи и набор связных с ней записей.
        Возьмем следующие примеси:
        SingleObjectMixin - даст нам сведения о выбранной записи
        ListView - даст нам набор связных с выбранной записью записей

"""

from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView
from .models import Poster, Rubric

class PosterByRubricView(SingleObjectMixin, ListView):
    template_name = 'board/by_rubric.html'
    pk_url_kwarg = 'rubric_id'
#   context_object_name = 'posters_pull' # Как в PosterByRubricView - Не получится, так как тут мы создаем
#                                         Указав новое имя для переменной, в этом атрибуте класса
    #                                     мы ЗАДАДИМ новое ИМЯ для переменной,
    #                                     в которой будет хранится рубрика, а НЕ НАБОР объявлений
    #                                     (Особенности языка)
#                                         Результат : ТРУДНО ДИАГНОСТИРУЕМАЯ ОШИБКА

    def get(self, request, *args, **kwargs):
        # Извлекаем рубрику с заданным ключом, сохраняем в атрибуте object нашего класса
        self.object = self.get_object(queryset=Rubric.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Заносим найденную в get() рубрику
        context['current_rubric'] = self.object
        # Сохраняем набор всех рубрик
        context['rubrics'] = Rubric.objects.all()
        # Создаем пееременную контекста шаблона и присваиваем ей набор записей, выводимых контроллером ListView
        context['posters_pull'] = context['object_list']
        return context

    # Возвращаем набор объявлений, связных с найденной рубрикой и полученных через диспетчер обратной связи
    def get_queryset(self):
        return self.object.poster_set.all()