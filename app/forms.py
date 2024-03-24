from django import forms

class ArtForm(forms.Form):
    profesion_oficio = forms.CharField(max_length=40,required=True)
    codigo_postal = forms.CharField(max_length=7,required=True)
    matricula = forms.CharField(max_length=40,required=True)
    año = forms.IntegerField(required=True)

class AutoForm(forms.Form):
    marca_del_auto= forms.CharField(max_length=40,required=True)
    año = forms.IntegerField(required=True)
    precio = forms.DecimalField(max_digits=50, decimal_places=2,required=True)
    modelo = forms.CharField(max_length=20,required=True)
    codigo_postal = forms.CharField(max_length=7,required=True)


class VidaForm(forms.Form):
    nombre= forms.CharField(max_length=40,required=True)
    apellido = forms.CharField(max_length=40,required=True)
    opciones_documento = (
        ('Documento Nacional de Identidad','Documento Nacional de Identidad'),
        ('Libreta Civica','Libreta Civica'),
        ('Libreta de Enrolamiento','Libreta de Enrolamiento'),
        ('CUIT','CUIT')
    )
    tipo_documento = forms.ChoiceField(choices=opciones_documento,required=True)
    n_numero = forms.IntegerField(required=True)
    n_celular = forms.IntegerField(required=True)
    correo_electronico=forms.EmailField(max_length=50)
    edad=forms.IntegerField(required=True)


class HogarForm(forms.Form):
    metros_cubiertos = forms.DecimalField(max_digits=10,decimal_places=2,required=True)
    codigo_postal = forms.CharField(max_length=10,required=True)
    año = forms.IntegerField()
    opciones_propiedad=(
        ('Departamento_Dos_Ambientes','Departamento_Dos_Ambientes'),
        ('Casa','Casa'),
        ('PH','PH'),
        ('Departamento_Tres_Ambientes','Departamento_Tres_Ambientes'),
        ('Departamento_Cuatro_Ambientes','Departamento_Cuatro_Ambientes'),
    )
    tipo_propiedad=forms.ChoiceField(choices=opciones_propiedad,required=True)

