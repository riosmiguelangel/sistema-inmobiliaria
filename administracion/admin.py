from django.contrib import admin

# Register your models here.
from administracion.models import TipoOperacion,Propiedades
from administracion.models import TipoAmbientes,TipoBarrio,TipoPropiedad,TipoProvincia, ImagenesPropiedades, Prueba
from django.contrib.auth.models import Group,User
# from django.contrib.auth.admin import GroupAdmin, UserAdmin


class ImagenesPropiedadAdmin(admin.TabularInline):
    model= ImagenesPropiedades

class PropiedadesAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_interno','descripcion','tipo_operacion', )
    list_filter = ['tipo_operacion'  'tipo_propiedad','tipo_ambiente',]
    search_fields = ['id', 'codigo_interno']
    list_per_page = 5  
    inlines= [
        ImagenesPropiedadAdmin
    ]

class TipoAmbientesAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion' )
    list_per_page = 5  

class TipoBarrioAdmin(admin.ModelAdmin):
    list_display = ('id_provincia','id','descripcion' )
    list_per_page = 5  


class TipoOperacionAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion' )
    list_per_page = 5  

class TipoPropiedadAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion' )
    list_per_page = 5  

class TipoProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion' )
    list_per_page = 5  

class ProvinciasAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')

class PruebaAdmin(admin.ModelAdmin):
     list_display = ('id', 'titulo')



""" admin.site.register(FotosChicaPropiedad,FotosChicaPropiedadAdmin)
admin.site.register(FotosMedianaPropiedad,FotosMedianaPropiedadAdmin) """
# admin.site.register(FotosPropiedad,FotosPropiedadAdmin)
admin.site.register(Propiedades,PropiedadesAdmin)
admin.site.register(TipoAmbientes,TipoAmbientesAdmin)
admin.site.register(TipoBarrio,TipoBarrioAdmin)
admin.site.register(TipoOperacion,TipoOperacionAdmin)
admin.site.register(TipoPropiedad,TipoPropiedadAdmin)
admin.site.register(TipoProvincia,TipoProvinciaAdmin)
admin.site.register(Prueba,PruebaAdmin)

