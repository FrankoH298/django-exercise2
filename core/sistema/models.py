from django.db import models

# Create your models here.
class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    Calle = models.CharField(max_length=50)
    Numero = models.PositiveIntegerField()
    Comuna = models.CharField(max_length=5)
    Ciudad = models.CharField(max_length=20)
    
    def __str__(self):
        return ("ID: {} | {} {} | {}".format(self.id, self.Calle, self.Numero, self.Ciudad))
        
    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"

class Proveedor(models.Model):
    RUT = models.PositiveIntegerField(primary_key=True)
    Nombre = models.CharField(max_length=15)
    Direccion = models.ForeignKey('Direccion', on_delete = models.CASCADE,)
    Telefono = models.BigIntegerField()
    WEB = models.CharField(max_length=200)
    
    def __str__(self):
        return ("RUT: {} | {} | Telefono: {}".format(self.RUT, self.Nombre, self.Telefono))
        
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"