
from django.urls import path
from votacao.views import index, resultados, equipe

urlpatterns = [
    path('', index),
    path('votar/', index),
    path('resultados/', resultados),
    path('equipe/', equipe),


]
