# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Prospecto(models.Model):
	nombre = models.CharField(max_length=120,  blank=False, null=True)#blank=False hace obligatorio el campo
	#apellido = models.CharField(max_length=120, blank=False, null=True)
	email = models.EmailField(blank=False)
	celular = models.CharField(max_length=120, blank=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	profesion = models.CharField(max_length=120, null=True, blank=True)
	state = models.CharField(max_length=120, null=True, blank=True)

	def __str__(self):
		return self.email
