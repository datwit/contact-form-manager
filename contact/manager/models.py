from django.db import models

# Create your models here.

class ContactData(models.Model):
    email= models.EmailField()
    name= models.CharField(max_length=100)
    subject= models.CharField(max_length=200)
    message= models.CharField(max_length=10000)
