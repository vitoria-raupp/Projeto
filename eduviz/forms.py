from django import forms

YEARS = [(year, year) for year in range(2014, 2022)]
STATES = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
]
PARAMETERS = [
    ('in_computador', 'Computador'),
    # Adicione outros parâmetros aqui se necessário
]

class DataForm(forms.Form):
    start_year = forms.ChoiceField(choices=YEARS, label='Ano Inicial')
    end_year = forms.ChoiceField(choices=YEARS, label='Ano Final')
    states = forms.MultipleChoiceField(choices=STATES, widget=forms.CheckboxSelectMultiple, label='Estados')
    parameter = forms.ChoiceField(choices=PARAMETERS, label='Parâmetro')
