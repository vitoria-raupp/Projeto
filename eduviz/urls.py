from django.urls import path
from . import views

urlpatterns = [
    path('line_chart/', views.line_chart, name='line_chart'),
    path('grafico_barras/', views.grafico_barras, name='grafico_barras'),
]
