from django.http import HttpResponse


def docedeleite(request):
    return HttpResponse("Dulce d'leite")


def novodoce(request):
    return HttpResponse("Inovação no sabor")

def leite_com_goiaba(request):
    return HttpResponse("Pensem numa delicia rsrsrsrsrsrs")

def ainda_tem_doce(request):
    return HttpResponse("Aproveite enquanto tem!!!!!!!!!!!!!!!!!!!!!!")