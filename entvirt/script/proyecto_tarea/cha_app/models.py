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
        return "{} {}".format(self.nombres, self.apellidos)

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
        return "{} {}".format(self.nombres, self.apellidos)

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

    def __str__(self):
        return "{} ".format(self.descripcion.upper())


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

    def __str__(self):
        return "{}".format(self.descripcion.upper())


class ContratoPoliza(models.Model):
    id_poliza = models.ForeignKey('Poliza', on_delete=models.CASCADE, null=False)
    id_vendedor = models.ForeignKey('Vendedor', on_delete=models.CASCADE, null=False)
    id_asegurado = models.ForeignKey('Asegurado', on_delete=models.CASCADE, null=False)
    fecha_contrato = models.DateField(null=False, blank=False)
    fecha_inicio = models.DateField(null=False, blank=False)
    fecha_fin = models.DateField(null=False, blank=False)
    estado = models.BooleanField(default=True)

    class Meta:
        ordering = ["id_poliza"]
        verbose_name_plural = "Contratos"

    def __str__(self):
        return "{} - {}{}".format(self.id_poliza.descripcion, self.id_asegurado.nombres, self.id_asegurado.apellidos)


class Doctor(models.Model):
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
        return "{} {}".format(self.nombres, self.apellidos)

    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Doctor, self).save()


class Familiares(models.Model):
    asegurado = models.ForeignKey('Asegurado', on_delete=models.CASCADE, null=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    estado = models.BooleanField(default=True)

    nombres = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    apellidos = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["asegurado"]
        verbose_name_plural = "Asegurados"

    def __str__(self):
        return "{}{}{} ".format(self.asegurado.nombres, self.nombres, self.apellidos)


class Hospitalizacion(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, null=False)
    contrato = models.ForeignKey('ContratoPoliza', on_delete=models.CASCADE, null=False)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, null=False)
    fecha_entrada = models.DateField(null=False, blank=False)
    fecha_salida = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Hospitalizaciones"

    def __str__(self):
        return "{} {} {} {} ".format(self.contrato.id_asegurado,self.hospital.descripcion,  self.fecha_entrada, self.fecha_salida)


class Tratamiento(models.Model):
    descripcion = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Tratamientos"

    def __str__(self):
        return "{}".format(self.descripcion)


class DetalleTratamiento(models.Model):
    hospitalizacion = models.ForeignKey('Hospitalizacion', on_delete=models.CASCADE, null=False)
    tratamiento= models.ForeignKey('Tratamiento', on_delete=models.CASCADE, null=False)
    descripcion = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    fecha = models.DateField(null=False, blank=False)
    costo = models.FloatField(default=0)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "DetalleTratamientos"

    def __str__(self):
        return "{}".format(self.descripcion)