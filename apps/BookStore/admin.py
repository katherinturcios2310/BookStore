from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
#Modelo1
class resourcelibros (resources.ModelResource):
    class Meta:
        model = libros

class adminlibros(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ['titulo', 'descripcion', 'linklibro', 'fk_autores', 'fk_editoriales']
    resource_class = resourcelibros

admin.site.register(libros, adminlibros)

#Modelo2
class resourceautores (resources.ModelResource):
    class Meta:
        model = autores

class adminautores(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['autor']
    list_display = ['autor']
    resource_class = resourceautores

admin.site.register(autores, adminautores)

#Modelo3
class resourcecategorias (resources.ModelResource):
    class Meta:
        model = categorias

class admincategorias(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['categoria']
    list_display = ['categoria']
    resource_class = resourcecategorias

admin.site.register(categorias, admincategorias)

#Modelo4
class resourceeditoriales (resources.ModelResource):
    class Meta:
        model = editoriales

class admineditoriales(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['editorial']
    list_display = ['editorial']
    resource_class = resourceeditoriales

admin.site.register(editoriales, admineditoriales)