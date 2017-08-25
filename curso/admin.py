# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Prospecto # Importando al administrador el modelo que cree
from .form import ProspectoForm # importando al admin el formulario desde forms


class ProspectoAdmin(admin.ModelAdmin):
	list_display = ["__str__","nombre", "celular", "state"]#esta lista es para poner en la tabla del administrador los datos que estamos recopilando
	form = ProspectoForm
	#class Meta:
		#model = Prospecto # aca estoy diciendo que el modelo que recopila la data es Prospecto

admin.site.register(Prospecto, ProspectoAdmin)# esto es para poner las 2 clases que estoy llamando al administrador