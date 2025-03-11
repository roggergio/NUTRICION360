"""
URL configuration for nutricionComplete project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('registroNutri', views.registroNutri, name='registroNutri'),
    path('price', views.price, name='price'),
    path('carrito', views.carrito, name='carrito'),
    path('navBar', views.navBar),
    path('aside_1', views.aside_1),
    path('aside_2', views.aside_2),

    path('pacientes', views.pacientesList, name='pacientes'),
    path('home', views.home, name='home'),
    path('datos_generales', views.datos_generales, name="datos_generales"),
    path('consultar', views.consultar, name='consultar'),
    path('equivalentes', views.equivalentes, name= 'equivalentes'),
    path('equivalentesRenal', views.equivalentesRenal, name= 'equivalentesRenal'),
    path('macronutrientes', views.macronutrientes, name='macronutrientes'),
    path('enfermedades', views.enfermedades, name='enfermedades'),
    path('habitos', views.habitos, name='habitos'),
    path('quimica_sanguinea', views.quimica_sanguinea, name='quimica_sanguinea'),
    path('alergiasYAdicciones', views.alergiasYAdicciones, name='alergiasYAdicciones'),
    path('bioquimicosPaciente', views.bioquimicosPaciente, name='bioquimicosPaciente'),
    path('antecedentesPatologicos', views.antecedentesPatologicos, name='antecedentesPatologicos'),
    path('antropometria', views.antropometria, name='antropometria'),
    path('medicamentos', views.medicamentos, name='medicamentos'),
    path('medicamentosPaciente', views.medicamentosPaciente, name='medicamentosPaciente'),
    path('r24', views.r24, name='r24'),
    path('energiaActividad', views.energiaActividad, name='energiaActividad'),
    path('tiemposComida', views.tiemposComida, name='tiemposComida'),

]
