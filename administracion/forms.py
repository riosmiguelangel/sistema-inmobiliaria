from xml.dom import ValidationErr
from django import forms
from .models import Propiedades, TipoAmbientes,TipoBarrio,TipoOperacion,TipoPropiedad,TipoProvincia, ImagenesPropiedades
from django.contrib.auth.models import User
from PIL import Image

class PropiedadesForm(forms.ModelForm):
    #codigo_externo = forms.CharField(error_messages={'required':'Hello! no te olvide de mi!'})
    codigo_interno = forms.CharField(
        label='Codigo: ', 
        max_length=255,
            widget=forms.TextInput(
                    attrs={'class':'form-control','placeholder':'Ingrese el codigo interno', 'rows' : '2'})
    )

    tipo_operacion = forms.ModelChoiceField(
        queryset=TipoOperacion.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='Seleccione una opcion'
    )
    
    tipo_propiedad = forms.ModelChoiceField(
        queryset=TipoPropiedad.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='Seleccione una opcion'
    )

    tipo_provincia = forms.ModelChoiceField(
        queryset=TipoProvincia.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='Seleccione una opcion'
    )

    tipo_barrio = forms.ModelChoiceField(
        queryset=TipoBarrio.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='Seleccione una opcion'
    )

    tipo_ambiente = forms.ModelChoiceField(
        queryset=TipoAmbientes.objects.all(),
        widget=forms.Select(attrs={'rows': 1,'class': 'form-control'}),
        initial='Seleccione una opcion'
    )

    calle = forms.CharField(
        label='Calle: ', 
        max_length=255,
            widget=forms.TextInput(
                    attrs={'class':'form-control','placeholder':'Ingrese el nombre de la calle', 'rows' : '2'})
    )

    altura = forms.IntegerField(
        label='Altura: ', 
            widget=forms.NumberInput (
                    attrs={'class':'form-control','placeholder':'Ingrese la altura (Número)', 'rows' : '2'})
    )
    
    piso = forms.CharField(
        label='Piso: ', 
        max_length=255,
            widget=forms.TextInput(
                    attrs={'class':'form-control','placeholder':'Ingrese el numero de piso', 'rows' : '2'})
    )

    depto = forms.CharField(
        label='Departamento: ', 
        max_length=255,
            widget=forms.TextInput(
                    attrs={'class':'form-control','placeholder':'Ingrese el número o letra del departameno', 'rows' : '2'})
    )

    torre = forms.CharField(
        label='Torre: ', 
        max_length=255,
            widget=forms.TextInput(
                    attrs={'class':'form-control','placeholder':'Ingrese la torre ', 'rows' : '2'})
    )

    valor = forms.IntegerField(
        label='Valor: ', 
            widget=forms.NumberInput (
                    attrs={'class':'form-control','placeholder':'Ingrese el valor ', 'rows' : '2'})
    )

    #fecha_alta = forms.DateTimeField()
    moneda = forms.CharField(
        label='Moneda: : ', 
        initial='U$S',
        
            widget=forms.TextInput(
                    attrs={'class':'form-control','placeholder':'Ingrese tipo de moneda ', 'rows' : '2'})

    )
    #reservado = forms.IntegerField()
    reservado = forms.BooleanField(
        label='Reservado: ',
    )

    descripcion = forms.CharField(
        label='Descripcion: ',
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 5,'class':'form-control'})
    )



    def clean_calle(self):
        pass
    
    class Meta:
        model=Propiedades
        fields=['codigo_interno',
                'tipo_operacion',
                'tipo_propiedad',
                'tipo_ambiente',
                'tipo_provincia',
                'tipo_barrio',
                'calle',
                'altura',
                'piso',
                'depto',
                'torre',
                'valor',
                'moneda',
                'reservado',
                'descripcion']
       # widgets = {
        #    'calle' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la calle'})
        #}
        error_messages = {
            'tipo_operacion' :{
                'required':'No te olvides de mi!'
            }
        }

class UploadImagenesPropiedadesForm(forms.ModelForm):
    label='id propiedad: ',    
    propiedadimg = forms.ModelChoiceField(
        queryset=Propiedades.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='Seleccione una opcion'
    )

    class Meta:
        model=ImagenesPropiedades
        fields=['imagen','propiedadimg']


