# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#Para renderizar los HTMLs que las vistas aca manejan.
from django.shortcuts import render
#Para importar como tal el formulario
from .form import *
#Para importar la funcionalidades de correos
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
#para validar el formulario
from django import forms
#Para traer los templates de los correos
from django.template.loader import render_to_string
#Para acceder a la URL de los documentos adjuntos
import urllib2
#Para redirigir despues a la pagina de agradecimiento.
from django.http import HttpResponseRedirect#Para redirigir despues a la pagina de agradecimiento.

# Create your views here.
def  landing_analytics(request):#Funcion para decir que renderice un html
	return render(request, "index.html", {})

def formulario(request): # Funcion para que renderice otro html
	#Estoy llamando el formulario que cree en forms.py y que ya tiene vinculado el modelo
	formulario_prospecto = ProspectoForm(
    	request.POST or None,
    	initial={#Con los initial estoy capturando los parametros de la URL
    		"source": request.GET.get("utm_source"),#capturando el parametro utm_source y guardandolo el el campo del formulario "source"
    		"medium": request.GET.get("utm_medium"),#capturando el parametro utm_medium y guardandolo el el campo del formulario "medium"
    		"campaign": request.GET.get("utm_campaign"),#capturando el parametro utm_campaign y guardandolo el el campo del formulario "campaign"
    		"content": request.GET.get("utm_content"),#capturando el parametro utm_content y guardandolo el el campo del formulario "content"
		}
	)
	#Un if condicional para validar si el formulario se diligencio
	if formulario_prospecto.is_valid():
		#Si el formulario se diligencio, lo guardo con el metodo .save()
		instance = formulario_prospecto.save()
		print "instance ={!r}".format(instance)
		#Capturo el correo que se metio en el formulario, usando un metodo que hice en la clase de forms.py
		email_prospecto = formulario_prospecto.clean_email()
		#Capturo el nombre que se metio en el formulario, usando un metodo que hice en la clase de forms.py
		nombre = formulario_prospecto.name_register()
		#Capturo el celular que se metio en el formulario, usando un metodo que hice en la clase de forms.py
		celular = formulario_prospecto.clean_celular()
		
		#ENVIO DEL CORREO 1 - CLIENTE
		#ELEMENTOS DEL CORREO 1
		#asunto:
		subject1= "Ya estas mas cerca de ser un experto en Google Analytics"
		#remitente:
		from_email1 = "cursos@mostaza.com.co"
		#destinatario, En este caso es el correo que capture en el formulario
		to_email1 = [email_prospecto]

		#TEMPLATES DEL CORREO
		#template como archivo txt con su contexto
		plantext1=render_to_string("mail-cliente.txt", {"nombre":nombre})
		#template como html con su contexto
		html1 = render_to_string("mail-cliente.html", {"nombre":nombre})

		#Clase para montar el objeto Correo
		email1 = EmailMultiAlternatives(subject1, plantext1,from_email1,to_email1)
		#hago que el Objeto correo que cree se envie en HTML
		email1.attach_alternative(html1,"text/html")

		#PDF ADJUNTO
		#Acceder a la URL donde esta el documento
		response = urllib2.urlopen("https://s3-us-west-1.amazonaws.com/mostazalanding/plan_estudios_curso_analytics.pdf")
		#Adjuntar el documento al correo
		email1.attach('plan_estudios_analytics.pdf', response.read(), mimetype="application/pdf")
		
		#ENVIO DEL CORREO 1
		#Metodo para enviar el primer correo
		email1.send()

		#ENVIO DEL CORREO 2 - EQUIPO COMERCIAL
		#ELEMENTOS DEL CORREO 2
		#Asunto:
		subject2="Hay un nuevo interesado en el curso de Google Analytics"
		#Remitente:
		from_email2="cursos@mostaza.com.co"
		#Destinatario:
		to_email2 = ["cursos@mostaza.com.co","mperalta@mostaza.com.co"]

		#TEMPLATES DEL CORREO 2
		#Template como archivo txt con sus contextos
		plantext2=render_to_string("mail-equipo.txt", {"nombre": nombre, "correo": email_prospecto, "celular":celular})
		html2 = render_to_string("mail-equipo.html", {"nombre": nombre, "correo": email_prospecto, "celular":celular})

		#Clase para montar el objeto de correo
		email2 = EmailMultiAlternatives(subject2,plantext2,from_email2,to_email2)
		#Hago que el objeto correo que cree se envio en HTML
		email2.attach_alternative(html2,"text/html")

		#ENVIO DEL CORREO 2
		#Metodo para enviar el segundo correo
		email2.send()

		#Aca estoy redirigiendo a la pagina de agradecimiento por que en el form del html redirijo a mi mismo para hacer el envio de los correos y el store de los datos
		return HttpResponseRedirect("/formulario/thankyou/")

	#Creo un diccionario que funcionara como contexto.
	context = {"form":formulario_prospecto}
	
	return render(request, "form.html",context)#Renderizo el HTML y el contexto definido.

def thankyou(request):
	return render(request, "thankyou.html", {})