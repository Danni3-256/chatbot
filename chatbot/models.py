from django.db import models

class chatbot(models.Model):
    destination = models.CharField(max_length=200)
    accomodation = models.CharField(max_length=200)
    
