"""mostaza_landing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from curso.views import * # estoy importando todo lo que hay en el archivo views de la carpeta curso

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^curso_analytics$',landing_analytics, name='landing_analytics'),
    url(r'^formulario/$',formulario, name='form'),# aca estoy diciendo que en esa url renderice la funcion home de curso.views
    url(r'^formulario/thankyou/$',thankyou, name='thankyou')
]