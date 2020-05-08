from django.db import models

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        unique=True
    )

    def __str__(self):
        return "{}".format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria,self).save()

    class Meta:
        verbose_name_plural="Categorias"
    
class SubCategoria(models.Model):
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )

    def __str__(self):
        return "{} --> {}".format(self.categoria, self.descripcion)
    
    class Meta:
        verbose_name_plural = "Sub Categorias"