from django.urls import path, re_path, include
from . import views
from django.contrib.auth.decorators import login_required

from django.conf.urls.static import static
from django.conf import settings
# from administracion.admin import sitio_admin

urlpatterns = [
    
    path('', views.index_administracion,name='index_administracion'),
    path('propiedades/index', views.propiedades_index,name='propiedades_index'),
    path('propiedades/nuevo', views.propiedades_nuevo,name='propiedades_nuevo'),
    path('propiedades/editar/<int:id_propiedad>', views.propiedades_editar,name='propiedades_editar'),
    path('propiedades/eliminar/<int:id_propiedad>', views.propiedades_eliminar,name='propiedades_eliminar'),
    path('propiedades/tables', views.propiedades_index,name='tables'),
    path('propiedades/imagenes', views.upload_image_view,name='imagenes'),
    path('propiedades/upload', views.multipleImagesUpload,name='upload'),


    path('datatables', views.datatables,name='datatables'),
    path('list_propiedades', views.list_propiedades,name='list_propiedades'),
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
