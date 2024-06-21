from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
#from forms import CustomUserCreationForm

# Create your views here.
def index(request):
    return render(request, 'base.html')
def contato(request):
    return render(request, 'contato.html')
def pagina_brasil(request):
    return render(request, 'brasil.html')

def pagina_charts(request):
    return render(request, 'charts.html')

def pagina_historico(request):
    return render(request, 'Historico')

def pagina_login(request):
    return render(request,'Login.html')

def pagina_perfil(request):
    return render(request, '.html')
def teste(request):
    return render(request, 'teste.html')
def termos(request):
    return render(request, 'termos.html')