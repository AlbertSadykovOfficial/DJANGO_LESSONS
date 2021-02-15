from django.forms import ModelForm

from .models import Poster

class PosterForm(ModelForm):
    class Meta:
        model  = Poster
        fields = ('name', 'about', 'price', 'rubric')