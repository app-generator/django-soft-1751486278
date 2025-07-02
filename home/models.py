# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Calculadora De Vulnerabilidad(models.Model):

    #__Calculadora De Vulnerabilidad_FIELDS__
    ingreso familiar = models.IntegerField(null=True, blank=True)
    miembros con ingresos = models.IntegerField(null=True, blank=True)
    miembros sin ingresos = models.IntegerField(null=True, blank=True)
    vivienda 1 a 10 (10 calidad muy insuficiente = models.IntegerField(null=True, blank=True)
    nivel educativo promedio (0=primaria, 1=secundaria, 2=superior incompleta, 3=superior completa) = models.IntegerField(null=True, blank=True)
    salud/pensión (0=sí, 1=no) = models.IntegerField(null=True, blank=True)
    puntaje de vulnerabilidad = models.IntegerField(null=True, blank=True)
    conclusión a el hogar está dentro del 40% más vulnerable. = models.TextField(max_length=255, null=True, blank=True)
    conclusión b el hogar  no está dentro del 40% más vulnerable. = models.TextField(max_length=255, null=True, blank=True)

    #__Calculadora De Vulnerabilidad_FIELDS__END

    class Meta:
        verbose_name        = _("Calculadora De Vulnerabilidad")
        verbose_name_plural = _("Calculadora De Vulnerabilidad")



#__MODELS__END
