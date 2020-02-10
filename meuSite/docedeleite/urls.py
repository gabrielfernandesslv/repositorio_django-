from django.urls import path
from docedeleite.views import docedeleite, novodoce, leite_com_goiaba, ainda_tem_doce

urlpatterns = [
    path('', docedeleite),
    path('novodoce/', novodoce),
    path('leite_com_goiaba/', leite_com_goiaba),
    path('ainda_tem_doce/', ainda_tem_doce),


]
