"""
 Перенаправление

    Временное - После добавления объявления, кидаем на лавную страницу
    Постоянное- При переезде на новый адрес (переправляем на новое метонахождение)

    Временное (django.http):
        HttpResponseRedirect(<целевой интерет-адрес>[, status=302][, reason=None])
        Пример:
        HttpResponseRedirect(reverse('board:index'))

    Постоянное (django.http):
        HttpResponsePermanentRedirect(<целевой интерет-адрес>[, status=302][, reason=None])
        Пример:
        HttpResponsePermanentRedirect('http:///www.new_address.ru/')
"""