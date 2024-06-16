from django.contrib import admin
from django.urls import path
from eduviz import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index),
    path('', views.index),
    path('brasil/', views.pagina_brasil),
    path('compare/', views.pagina_compare),
    path('historico/', views.pagina_historico),
    path('login/', views.pagina_login),
    path('perfil/', views.pagina_perfil),
]
