from django.contrib import admin
from django.urls import path, include
from eduviz import views
from django.contrib.staticfiles.urls import static
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    # path('', include('core.urls')),
    path('', views.index),
    path('brasil/', views.pagina_brasil),
    path('historico/', views.pagina_historico),
    path('login/', views.pagina_login, name='login.html'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.pagina_perfil),
    path('teste/', views.teste),
    path('termos/', views.termos, name='termos.html'),
    path('charts/', views.pagina_charts, name='charts.html'),
    path('contato', views.contato, name='contato.html'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('Projeto.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('Projeto.urls')),

]

urlpatterns += staticfiles_urlpatterns()
