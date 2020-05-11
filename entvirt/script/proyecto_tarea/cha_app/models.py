from django.db import models


class Vendedor(models.Model):
    nombres = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    apellidos = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{}{}".format(self.nombres, self.apellidos)

    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Vendedor, self).save()

    class Meta:
        verbose_name_plural = "Vendedores"


class Asegurado(models.Model):
    nombres = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    apellidos = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    direccion = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    estado = models.BooleanField(default=True)
    fecha_nacimiento = models.DateField(null=False, blank=False)

    def __str__(self):
        return "{}{}{}".format(self.nombres, self.apellidos, self.fecha_nacimiento)

    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Asegurado, self).save()


class Poliza(models.Model):
    descripcion = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    costo = models.FloatField(default=0)
    costo_extension = models.FloatField(default=0)
    valor_cobertura = models.FloatField(default=0)


class Hospital(models.Model):
    descripcion = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    direccion = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    estado = models.BooleanField(default=True)


class ContratoPoliza(models.Model):
    id_poliza = models.ForeignKey('Poliza', on_delete=models.DO_NOTHING)
    id_vendedor = models.ForeignKey('Vendedor', on_delete=models.DO_NOTHING)
    id_asegurado = models.ForeignKey('Asegurado', on_delete=models.DO_NOTHING)
    fecha_contrato = models.DateField(null=False, blank=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    estado = models.BooleanField(default=True)