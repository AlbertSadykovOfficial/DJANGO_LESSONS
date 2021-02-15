"""
	Создание наборов форм, связанных с моделями

		Набор форм связанный с модулью помогает редактироват несколько записей,
		в отличие от обычных форм, который работаю тольок с 1 записью модели.

	Для созания таких форм применяется фабрика классов:
		modelformset_factory(<модель>[,
													form=<форма, связанная с моделью>][,
													exclude=None][,
													labels=None][,
													help_texts=None][,
													error_messages=None][,
													field_classes=None][,
													widgets=None][,
													extra=1][,
													can_order=False][,
													can_delete=False][,
													min_num=None][, validate_min=False][,
													max_num=None][, validate_max=False][,
													formset=<Набор форм, связаных с моделью>][,)
"""

# Набор форм, позволяющий за раз добавить 1 запись и изменить существующие:
from django.forms import modelformset_factory
from .models import Rubric

RubricFormSet = modelformset_factory(Rubric, fields=('name',))

# Набор форм, позволяющий добавлять 1 запись, удалять и переупорядочивать остальные

RubricFormSet = modelformset_factory(Rubric, fields=('name',), can_order=True, can_delete=True)

