from django.contrib import admin
from django.urls import path, include
from eduviz import views
from django.contrib.staticfiles.urls import static
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('core.urls')),
    path('', views.index),
    path('brasil/', views.pagina_brasil),
    path('compare/', views.pagina_compare),
    path('historico/', views.pagina_historico),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.pagina_perfil),
    path('teste/', views.teste),
]

urlpatterns += staticfiles_urlpatterns()
