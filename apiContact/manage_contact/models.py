import uuid
from django.db import models

# Create your models here.

class contact_data(models.Model):
	# Django create by default id as primary key
	ref_hash= models.UUIDField(default=uuid.uuid4)
	email= models.EmailField(blank= False)
	name= models.CharField(max_length=100)
	subject= models.CharField(max_length=200, blank= False)
	message= models.TextField(max_length=10000, blank= False)
	attended= models.BooleanField(default= False)
	active= models.BooleanField(default= True)
	created_at= models.DateTimeField(auto_now_add= True)
	updated_at= models.DateTimeField(auto_now= True)

class answer_data(models.Model):
	user_name= models.CharField("user",max_length=50)
	answer= models.CharField(max_length=1000)
	created_at= models.DateTimeField(auto_now_add= True)
	answer_to=models.IntegerField(default='0')