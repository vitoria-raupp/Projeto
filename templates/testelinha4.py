import plotly.express as px
import pandas as pd

# Gerar dados fictícios para vários estados de 2013 a 2023
estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
anos = (2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023)

data = []
for estado in estados:
    for ano in anos:
        valor = np.random.randint(100, 1000)  # Dados fictícios
        data.append([estado, ano, valor])

df = pd.DataFrame(data, columns=['Estado', 'Ano', 'Valor'])

# Criar o gráfico de linha interativo com dropdown
fig = px.line(df, x='Ano', y='Valor', color='Estado', title='Evolução dos Dados por Estado (2013-2023)', labels={'Valor': 'Valor', 'Ano': 'Ano'})

# Adicionar dropdown para selecionar o estado
fig.update_layout(
    updatemenus=[
        {
            'buttons': [
                {
                    'args': [{'visible': [estado == e for e in estados]}],
                    'label': estado,
                    'method': 'update'
                }
                for estado in estados
            ],
            'direction': 'down',
            'showactive': True,
        }
    ]
)

# Salvar o gráfico como um arquivo HTML
html_path = '/mnt/data/grafico_interativo_estados.html'
fig.write_html(html_path)

html_path
