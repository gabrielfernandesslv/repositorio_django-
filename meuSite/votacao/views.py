from django.http import HttpResponse


def index(request):
    return HttpResponse("oiiiiiiie")


def resultados(request):
    return HttpResponse("Resultados")


def equipe(request):
    return HttpResponse("Érica Vitória <br>Gabriel Fernandes")
