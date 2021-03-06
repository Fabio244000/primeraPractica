"""miSitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from miSitio.views import  *
from django.contrib import admin
from biblioteca import views
from contactos.views import contactos

urlpatterns = [
    #url(r'^hola/$', hola),
    #url(r'^$', raiz),
    #url(r'^fecha/mas/\d{1,2}/$', horas_adelante ),
    #url(r'^fecha/$',fecha_actual),
    url(r'^admin/', admin.site.urls),
    #url(r'^atributos/$', atributos_meta),
    #url(r'^navegador/$',mostrar_navegador),
    #url(r'^navegador1/$', mostrar_navegador2),
    #url(r'^formulario-buscar/', views.formulario_buscar),
    url(r'^buscar/$', views.buscar),
    url(r'^contactos/$',contactos),

    
]