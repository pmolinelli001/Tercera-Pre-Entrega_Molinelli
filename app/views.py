from django.shortcuts import render, redirect
from .models import*
from .forms import*
# Create your views here.

def home(request):
    return render(request,"app/index.html")

def art(request):
    contexto = {'Art': Art.objects.all()}
    return render(request,"app/art_list.html",contexto)

def auto(request):
    contexto = {'Auto': Auto.objects.all()}
    return render(request,"app/auto_list.html",contexto)

def autoForm(request):
    if request.method  == 'POST':
        miForm = AutoForm(request.POST)
        if miForm.is_valid():
            auto_marca_del_auto=miForm.cleaned_data.get("marca_del_auto")
            auto_año=miForm.cleaned_data.get("año")
            auto_precio=miForm.cleaned_data.get("precio")
            auto_codigo_postal=miForm.cleaned_data.get("codigo_postal")
            auto=Auto(marca_del_auto=auto_marca_del_auto,año=auto_año,precio=auto_precio,codigo_postal=auto_codigo_postal)
            auto.save()
            contexto={'auto':Auto.objects.all()}
            return render(request,"app/index.html")
    else:
        miForm =AutoForm()
    return render(request,'app/autoForm.html',{"form":miForm})

def autocob(request):
    todo_riesgo = TodoRiesgo.objects.all()
    cobertura_parcial = CoberturaParcial.objects.all()
    return render(request, 'app/autocob.html', {'todo_riesgo':todo_riesgo, 'cobertura_parcial': cobertura_parcial})


def hogar(request):
    contexto = {'Hogar': Hogar.objects.all()}
    return render(request,"app/hogar_list.html",contexto)

def hogarForm(request):
    if request.method  == 'POST':
        miForm = HogarForm(request.POST)
        if miForm.is_valid():
            hogar_metros_cubiertos=miForm.cleaned_data.get("metros_cubiertos")
            hogar_codigo_postal=miForm.cleaned_data.get("codigo_postal")
            hogar_año=miForm.cleaned_data.get("año")
            hogar_tipo_propiedad=miForm.cleaned_data.get("tipo_propiedad")
            hogar=Hogar(metros_cubiertos=hogar_metros_cubiertos,codigo_postal=hogar_codigo_postal,año=hogar_año,tipo_propiedad=hogar_tipo_propiedad)
            hogar.save()
            contexto={'hogar':Hogar.objects.all()}
            return render(request,"app/index.html")
    else:
        miForm =HogarForm()
    return render(request,'app/hogarForm.html',{"form":miForm})

def hogarcob1(request):
    departamento_dos_amb = Departamento_Dos_Ambientes.objects.all()
    return render(request, 'app/hogarcob1.html', {'departamento_dos_amb':departamento_dos_amb})

def hogarcob2(request):
    departamento_tres_amb = Departamento_Tres_Ambientes.objects.all()
    return render(request, 'app/hogarcob2.html', {'departamento_tres_amb':departamento_tres_amb})

def hogarcob3(request):
    departamento_cuatro_amb = Departamento_Cuatro_Ambientes.objects.all()
    return render(request, 'app/hogarcob3.html', {'departamento_cuatro_amb':departamento_cuatro_amb})

def hogarcob4(request):
    casa = Casa.objects.all()
    return render(request, 'app/hogarcob4.html', {'casa':casa})

def hogarcob5(request):
    ph = Ph.objects.all()
    return render(request, 'app/hogarcob5.html', {'ph':ph})

def consultar_hogar(request):
    if request.method == 'POST':
        tipo_propiedad = request.POST.get('tipo_propiedad')
        if tipo_propiedad == 'Departamento_Dos_Ambientes':
            return redirect('hogarcob1')
        elif tipo_propiedad == 'Casa':
            return redirect('hogarcob4')
        elif tipo_propiedad == 'PH':
            return redirect('hogarcob5')
        elif tipo_propiedad == 'Departamento_Tres_Ambientes':
            return redirect('hogarcob2')
        elif tipo_propiedad == 'Departamento_Cuatro_Ambientes':
            return redirect('hogarcob3')        
    return redirect('home')



def Quienes_somos(request):
    return render(request,"app/quienes_somos.html")

def vida(request):
    contexto = {'Vida': Vida.objects.all()}
    return render(request,"app/vida_list.html", contexto)

def vidaForm(request):
    if request.method  == 'POST':
        miForm = VidaForm(request.POST)
        if miForm.is_valid():
            vida_nombre=miForm.cleaned_data.get("nombre")
            vida_apellido=miForm.cleaned_data.get("apellido")
            vida_tipo_documento=miForm.cleaned_data.get("tipo_documento")
            vida_n_numero=miForm.cleaned_data.get("n_numero")
            vida_n_celular=miForm.cleaned_data.get("n_celular")
            vida_correo_electronico=miForm.cleaned_data.get("correo_electronico")
            vida_edad=miForm.cleaned_data.get("edad")
            vida=Vida(nombre=vida_nombre,apellido=vida_apellido,tipo_documento=vida_tipo_documento,n_numero=vida_n_numero,n_celular=vida_n_celular,correo_electronico=vida_correo_electronico,edad=vida_edad)
            vida.save()
            contexto={'vida':Vida.objects.all()}
            return render(request,"app/index.html")
    else:
        miForm =VidaForm()
    return render(request,'app/vidaForm.html',{"form":miForm})



def MasInfo(request):
    return render(request,"app/mas_info.html")

def artForm(request):
    if request.method  == 'POST':
        miForm = ArtForm(request.POST)
        if miForm.is_valid():
            art_profesion_oficio= miForm.cleaned_data.get("profesion_oficio")
            art_codigo_postal= miForm.cleaned_data.get("codigo_postal")
            art_matricula=miForm.cleaned_data.get("matricula")
            art_año=miForm.cleaned_data.get("año")
            art=Art(profesion_oficio=art_profesion_oficio, codigo_postal=art_codigo_postal, matricula=art_matricula,año=art_año)
            art.save()
            contexto={'art':Art.objects.all()}
            return render(request,"app/index.html")
    else:
        miForm =ArtForm()
    return render(request,'app/artForm.html',{"form":miForm})

def artcob(request):
    dependiente = Dependiente.objects.all()
    independiente = TrabajoIndependiente.objects.all()
    return render(request, 'app/artcob.html', {'dependiente':dependiente, 'independiente': independiente})

def buscarArt(request):
    return render(request,"app/buscar.html")

def encontrarArt(request):
    if request.GET["buscar"]:
        patron=request.GET["buscar"]
        art=Art.objects.filter(profesion_oficio__icontains=patron)
        contexto ={"art":art}
        return render(request,"app/art_list.html",contexto)
    else:
        contexto = {'art': Art.objects.all()}
        return render(request,"app/art_list.html",contexto)
