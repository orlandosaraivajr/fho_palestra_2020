from django.shortcuts import render

from django.http import HttpResponse


def natal(request):
    contexto = {
        'natal':False,
        'carnaval':False,
    }
    return render(request, 'natal.html', contexto)

