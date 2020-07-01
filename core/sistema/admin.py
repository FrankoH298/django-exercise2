from django.contrib import admin
from sistema.models import *

# Register your models here.

admin.site.register(Direccion,)
admin.site.register(Proveedor,)
admin.site.register(Cliente,)
admin.site.register(Categoria,)
admin.site.register(Venta,)
admin.site.register(Producto,)