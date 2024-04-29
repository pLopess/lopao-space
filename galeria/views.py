from django.shortcuts import render


def index(request):
    return render(request, 'galeria/index.html')    #1° o request, 2° o q eu quero exibir