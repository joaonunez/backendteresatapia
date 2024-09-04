from django.db import models
#models
class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Trabajador(models.Model):
    id_trabajador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    direccion = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    fecha_ingreso = models.DateField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    licencia_conducir = models.BooleanField(default=False)
    observaciones = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
