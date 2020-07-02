from django.db import models

# Create your models here.

class direccion (models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    def __str__(self):
        return ("ID: {} / {} {} / {}".format(self.id, self.Calle, self.Numero, self.Ciudad))

class cliente (models.Model):
    RUT = models.AutoField(primary_key=True)
    direccion = models.ForeignKey('direccion', on delete = models.CASCADE)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_lengtj=11)
    def __str__(self):
        return ("RUT: {} / {} / telefono {}". format(self.RUT, self.nombre, self.telefono))

class proovedor (models.Model):
    RUT = models.AutoField(primary_key=True)
    direccion = models.ForeignKey('direccion', on delete= models.CASCADE)
    telefono = models.CharField(max_length=11)
    nombre = models.CharField(max_length=50)
    web = models.CharField(max_length=2.083)
    def __str__(self):
        return ("Rut: {} / {} / {} / {}". format(self.RUT, self.nombre, self.telefono, self.web))

class categoria (models.Model):
    ID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return ("ID: {} / {} / descripcion :{}".format(self.ID,self.nombre,self.descripcion))

class producto (models.Model):
    ID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = modesl.IntegerField()
    proveedor = models.ForeignKey('proveedor', on_delete = models.CASCADE, default = None)
    categoria = models.ForeignKey('categoria', on_delete = models.CASCADE, default = None)
    venta = models.ForeignKey('venta', on_delete = models.CASCADE, default = None)
    def __str__(self):
        return ("ID: {} / {} / {}".format(self.ID,self.nombre,self.precio))

class venta (models.Model):
    ID = models.AutoField(primary_key=True)
    fecha = models.DateField()
    monto_final = models.IntegerField()
    descuento = models.BooleanField
    cantidad = models.IntegerField()
    cliente = models.ForeignKey('cliente', on_delete = models.CASCADE, defautl=None)
    def __str__(self):
        return ("ID: {}/ ${}/ cantidad:{}".format(self.ID,self.monto_final,self.cantidad))
    