from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'contato.html')

def pagina_brasil(request):
    return HttpResponse('Brasil')

def pagina_compare(request):
    return render(request, 'compare.html')

def pagina_historico(request):
    return HttpResponse('Historico')

def pagina_login(request):
    return HttpResponse('Login')

def pagina_perfil(request):
    return render(request, 'login.html')
def teste(request):
    return render(request, 'teste.html')