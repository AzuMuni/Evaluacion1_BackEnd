from django.shortcuts import render

# Create your views here.

def mostrar_home(request):
    return render(request,'index.html')

def mostrar_servicio(request):
    datos = {
        "nombre": "Lavado de vehículos",
        "valor": 10000
    }
    return render(request, 'about.html', datos)



