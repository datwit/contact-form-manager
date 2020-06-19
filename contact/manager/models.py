import uuid
from django.db import models

# Create your models here.

class ContactData(models.Model):
	ref_number= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	email= models.EmailField(blank= False)
	name= models.CharField(max_length=100)
	subject= models.CharField(max_length=200, blank= False)
	message= models.TextField(max_length=10000, blank= False)
	attended= models.BooleanField(default= False)
	created_at= models.DateTimeField(auto_now_add= True)
	updated_at= models.DateTimeField(auto_now= True)
    
