from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Títuloum")
    description = models.TextField(verbose_name="Descripcioum")
    image = models.ImageField(upload_to="projects",  verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacionum")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicionum")
    link = models.URLField(max_length=200, null=True, blank=True, verbose_name="Direccion Webium")

    class Meta:
        verbose_name = "proyectumtumtum"
        verbose_name_plural = "proyecturiums"
        ordering = ["-created"]  # <=====

    def __str__(self):
        return self.title  # <=====

