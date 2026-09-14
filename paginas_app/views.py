from django.shortcuts import render

# Create your views here.

def mostrar_home(request):
    return render(request,'index.html')

def mostrar_servicio(request):
    datos = {
        "lav": "Lavado de vehículos:",
        "valorlav": 10000,

        "air": "Inflar ruedas: ",
        "valorair": "sin costo",

        "estacionamiento": "Estacionamiento",
        "valorest": "300 minimo, 500 por minuto, 1000 por hora "
    }
    return render(request, 'about.html', datos)



