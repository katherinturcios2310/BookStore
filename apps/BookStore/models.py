from django.db import models

# Create your models here.
class autores(models.Model):
    pk_autores = models.AutoField(primary_key=True, null=False, blank=False)
    autor = models.CharField(max_length=50, null=False, blank=False)

class categorias(models.Model):
    pk_categorias = models.AutoField(primary_key=True, null=False, blank=False)
    categoria = models.TextField(null=False, blank=False)

class editoriales(models.Model):
    pk_editoriales = models.AutoField(primary_key=True, null=False, blank=False)
    editorial = models.TextField(null=False, blank=False)

class libros(models.Model):
    pk_libros = models.AutoField(primary_key=True, null=False, blank=False)
    titulo = models.CharField(max_length= 50, null=False, blank=False)
    fk_autores = models.ForeignKey(autores, on_delete=models.CASCADE, null=False, blank=False)
    fk_categorias = models.ManyToManyField(categorias, blank=False)
    fk_editoriales = models.ForeignKey(editoriales, on_delete=models.CASCADE, null=False, blank=False)
    idioma = models.CharField(max_length=50, null=False, blank=False)
    paginas = models.IntegerField(null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    imagen = models.URLField(max_length=8000, blank=False, null=False, default='https://i.ibb.co/0JZN3GS/6034d7d1f3e0f54a99b2b2bd-Mujercitas-louisa-may-alcott-editorial-alma.jpg')
