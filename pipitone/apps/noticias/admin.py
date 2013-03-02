from django.contrib import admin
from pipitone.apps.noticias.models import categorias
from pipitone.apps.noticias.models import noticias

admin.site.register(categorias)
admin.site.register(noticias)