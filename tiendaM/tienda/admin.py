from django.contrib import admin
from .models import Cancion
from .models import Autor
from .models import Genero
# Register your models here
# .
admin.site.register(Cancion)
admin.site.register(Autor)
admin.site.register(Genero)
