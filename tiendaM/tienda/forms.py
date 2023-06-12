from django import forms
from .models import Cancion
from .models import Autor
from .models import Genero
class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields ='__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields ='__all__'

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields ='__all__'


