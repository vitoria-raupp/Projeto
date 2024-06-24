from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
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

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Autentica e loga o usuário automaticamente após o registro
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')  # Redireciona para a página inicial após o registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})