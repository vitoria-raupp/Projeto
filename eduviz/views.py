from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import plotly.express as px
import pandas as pd
from django.shortcuts import render
from .forms import DataForm

api_url = 'https://mutt-correct-mongoose.ngrok-free.app/data'

def get_data_from_api(parameter, estados, anos):
    data = []
    params = {
        'parameter': parameter,
        'estado': estados,
        'ano': anos
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        api_data = response.json()
        for ano, estados_data in api_data[parameter].items():
            for estado_data in estados_data:
                estado = estado_data['estado']
                valor = estado_data['count_not_equals_zero']
                data.append([estado, int(ano), parameter, valor])
    else:
        print(f"Erro ao obter dados da API: {response.status_code}")
        return None
    return data

def line_chart(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            start_year = form.cleaned_data['start_year']
            end_year = form.cleaned_data['end_year']
            states = form.cleaned_data['states']
            parameter = form.cleaned_data['parameter']

            anos = list(range(int(start_year), int(end_year) + 1))
            data = get_data_from_api(parameter, states, anos)

            if data:
                df = pd.DataFrame(data, columns=['Estado', 'Ano', 'Parâmetro', 'Valor'])
                fig = px.line(df, x='Ano', y='Valor', color='Estado', title=f'Dados de {parameter}')
                graph_html = fig.to_html(full_html=False)
            else:
                graph_html = '<p>Erro ao obter dados da API.</p>'
            
            return render(request, 'line_chart.html', {'form': form, 'graph_html': graph_html})
    else:
        form = DataForm()

    return render(request, 'line_chart.html', {'form': form})


# Create your views here.
def index(request):
    return render(request, 'base.html')

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
