from django.urls import path
from galeria.views import index

urlpatterns  = [
    path('', index)    #na pagina padrao vai chamar o index
]