from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    clientes = [
        {'nombre': 'Juan Pérez', 'destino_preferido': 'París'},
        {'nombre': 'María García', 'destino_preferido': 'Cancún'},
        {'nombre': 'Carlos Rodríguez', 'destino_preferido': 'Roma'},
    ]
    context = {'clientes': clientes}
    return render(request, 'index.html', context)