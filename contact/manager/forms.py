from django import forms
from .models import ContactData

class ContactForm(forms.ModelForm):
    class Meta:
        model= ContactData
        fields= ["email", "name", "subject", "message"]
