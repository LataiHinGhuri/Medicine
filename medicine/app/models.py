from django.db import models
from django.conf import settings
from django.urls import reverse

class MedicinePost(models.Model):
    # pk aka id --> numbers
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    name       = models.CharField(max_length=120, null=True, blank=True)
    description     = models.TextField(max_length=120, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    timedif = models.IntegerField(null=True,blank=True)

    def __str__(self):
    	return self.name

    
