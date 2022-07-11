from django.forms import ModelForm
from . import models

class MovieList(ModelForm):
    class Meta:
        model=models.Movie
        exclude=('user',)