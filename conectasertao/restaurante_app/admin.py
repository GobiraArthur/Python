from django.contrib import admin
from restaurante_app.models import * 

# Register your models here.
admin.site.register(Item)
admin.site.register(ItemCardapio)
admin.site.register(Cardapio)
admin.site.register(Categoria)