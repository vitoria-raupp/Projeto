from django.urls import path, include
from .views import index, contato
from django.contrib import admin


urlpatterns = [
     path('', index),
     path('contato', contato),
     path('accounts/', include('django.contrib.auth.urls')),
     path('', include('Projeto.urls')),
]