from django.contrib import admin
from sistema.models import Proveedor, Direccion, Cliente

# Register your models here.

admin.site.register(Direccion,)
admin.site.register(Proveedor,)
admin.site.register(Cliente,)