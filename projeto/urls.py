from django.contrib import admin
from django.urls import path
from eduviz import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('', views.index),
    path('brasil/', views.pagina_brasil),
    path('historico/', views.pagina_historico),
    path('login/', views.pagina_login, name='login.html'),
    path('perfil/', views.pagina_perfil),
    path('teste/', views.teste),
    path('termos/', views.termos, name='termos.html'),
    path('charts/', views.pagina_charts, name='charts.html'),

]

urlpatterns += staticfiles_urlpatterns()
