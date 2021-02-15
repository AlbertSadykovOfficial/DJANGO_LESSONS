"""
    Сокращение - функция, производящая сразу несколько действий и предназанченная для выполнения типичных задач

    Все сокращения Django:

        render(<запрос>, <путь к шаблону>[, context=None][, content_type=None][, status=200]) # Вернет HttpResponse
        Пример:
            render(request, 'board/create.html', context)

        redirect(<цель>[, permanent=False][, <значения URL-параметров>])
        Пример:
            redirect('board:by_rubric', rubric_id=poster.cleaned_data['rubric'].pk)

        get_object_or_404(<источник>, <условия поиска>)
        Пример:
            def detail(request, poster_id):
                poster=get_object_or_404(Poster, pk=poster_id)
                return HttpResponse(...)

        get_list_or_404(<источник>, <условия фильтрации>)
        Пример:
            def by_rubric(request, rubric_id):
                poster=get_list_or_404(Poster, rubric=rubric_id)
"""