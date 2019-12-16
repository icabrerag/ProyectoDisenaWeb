from django.db import models
from apps.compra.models import Persona



class Plan(models.Model): 
    plan = models.CharField(max_length=50)
    curso = models.CharField(max_length=30)
    tipo = models.CharField(max_length=50)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)

    