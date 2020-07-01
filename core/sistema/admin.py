from django.contrib import admin
from sistema.models import *

class ProveedorAdmin(admin.ModelAdmin):
    class EntryInLines(admin.TabularInline):
        model = Producto
    inlines = [EntryInLines,]
    
class ClienteAdmin(admin.ModelAdmin):
    class EntryInLines(admin.TabularInline):
        model = Venta
    inlines = [EntryInLines,]
    list_display = ['RUT', 'Nombre', 'Telefono']
    
class CategoriaAdmin(admin.ModelAdmin):
    class EntryInLines(admin.TabularInline):
        model = Producto
    inlines = [EntryInLines,]
    
class VentaAdmin(admin.ModelAdmin):
    class EntryInLines(admin.TabularInline):
        model = Producto
    inlines = [EntryInLines,]
    
class ProductoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descripcion', {
            'fields': ('ID', 'Nombre')
        }),
        ('Variables', {
            'fields': ('Precio', 'Stock',)
        }),
    )

# Register your models here.

admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Direccion,)