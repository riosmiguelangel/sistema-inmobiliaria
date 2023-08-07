from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse

from administracion.models import Propiedades,TipoAmbientes,TipoBarrio,TipoOperacion,TipoPropiedad,TipoProvincia,ImagenesPropiedades

from administracion.forms import PropiedadesForm,UploadImagenesPropiedadesForm


# Create your views here.
def upload_image_view(request):
    if request.method == 'POST':
        form = UploadImagenesPropiedadesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully!"
    else:
        form = UploadImagenesPropiedadesForm()

    return render(request,'administracion/propiedades/imagenes.html',{'form': form})


def multipleImagesUpload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')

        for image in images:
            ImagenesPropiedades.objects.create(imagen = image)

        uploaded_images = ImagenesPropiedades.objects.all()
        return JsonResponse({"images": [{"url": image.image.url} for image in uploaded_images]})
    return render(request, "administracion/propiedades/uploadimagen.html")



#@login_required
def index_administracion(request):
    variable = 'test variable'
    return render(request,'administracion/index_administracion.html',{'variable':variable})




"""
    datatables
"""
def datatables(request):
    return render(request, 'administracion/datatables.html')

def list_propiedades(request):
    propiedades=list(Propiedades.objects.values())
    #provincias=list(TipoProvincia.objects.values())
    data={'propiedades':propiedades }
    return JsonResponse(data)

def list_provincias(request):
    provincias=list(TipoProvincia.objects.values())
    data={'provincias':provincias}
    return JsonResponse(data)


"""
    CRUD propiedades
"""
# @login_required
def propiedades_index(request):
    #queryset
    propiedades = Propiedades.objects.all().select_related()
    #return render(request,'administracion/propiedades/index.html',{'propiedades': propiedades})
    return render(request,'administracion/propiedades/tables.html',{'propiedades': propiedades})


def propiedades_nuevo(request):
    if(request.method=='POST'):
        formulario = PropiedadesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('propiedades_index')
    else:
        formulario = PropiedadesForm()
    return render(request,'administracion/propiedades/nuevo.html',{'form':formulario})

def propiedades_editar(request,id_propiedad):
    try:
        propiedad = Propiedades.objects.get(pk=id_propiedad)
    except Propiedades.DoesNotExist:
        return render(request,'administracion/404_admin.html')

    if(request.method=='POST'):
        formulario = PropiedadesForm(request.POST,instance=propiedad)
        if formulario.is_valid():
            formulario.save()
            return redirect('propiedades_index')
    else:
        formulario = PropiedadesForm(instance=propiedad)
    return render(request,'administracion/propiedades/editar.html',{'form':formulario})

def propiedades_eliminar(request,id_propiedad):
    try:
       propiedad = Propiedades.objects.get(pk=id_propiedad)
    except Propiedades.DoesNotExist:
        return render(request,'administracion/404_admin.html')    
    propiedad.delete()
    return redirect('propiedades_index')

