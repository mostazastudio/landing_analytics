from django import forms # importar los formularios desde django
from .models import * # importar los modelos al formulario


class ProspectoForm(forms.ModelForm):
	class Meta:
		#Defino cual es el modelo que se vincula a este formulario
		model = Prospecto
		#Defino que campos de ese modelo voy a usar en este formulario
		fields = ["nombre","celular", "email"]
		#Con estos widgets, agrego los placeholders a cada campo
		widgets ={
			"nombre":forms.TextInput(attrs={"placeholder":"Nombre"}),
			#"apellido":forms.TextInput(attrs={"placeholder":"Apellidos"}),
			"celular":forms.TextInput(attrs={"placeholder":"Celular"}),
			"email":forms.TextInput(attrs={"placeholder":"Correo"}),

		}

	#Metodo del formulario para capturar el correo y usarlo para varias cosas.
	def clean_email(self):
		email= self.cleaned_data.get("email")
		
		#si quiero hacer una validacion de la informacion en ese campo la haria asi:
		#if not "edu" in email: # el valida si hay el string edu en la info capturada
			#raise forms.ValidationError("Por favor usa el correo de la Universidad") # si no, entonces lanza este error
		
		return email
	
	#Metodo del formulario para capturar el nombre y usarlo para varias cosas	
	def name_register(self):
		nombre=self.cleaned_data.get("nombre")
		return nombre

	#Metodo del formulario para capturar el nombre y usarlo para varias cosas		
	def clean_celular(self):
		celular=self.cleaned_data.get("celular")
		return celular