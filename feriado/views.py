from django.shortcuts import render

from django.http import HttpResponse


def natal(request):
    # return HttpResponse("<h1>Não é natal.</h1>")
    return render(request,'natal.html')
