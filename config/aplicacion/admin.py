from django.contrib import admin
from aplicacion.models import *


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['RUT', 'nombre', 'telefono']



# Register your models here.
admin.site.register(direccion,)
admin.site.register(cliente,ClienteAdmin,)
admin.site.register(provedor,)
admin.site.register(categoria,)
admin.site.register(producto,)
admin.site.register(venta,)