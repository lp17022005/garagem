from django.contrib import admin

from core.models import Marca, Categoria, Cores, Motores, Valor, Carro

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Cores)
admin.site.register(Motores)
admin.site.register(Valor)
admin.site.register(Carro)