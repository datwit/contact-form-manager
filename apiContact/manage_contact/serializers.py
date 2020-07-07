from django.contrib.auth.models import User, Group
from rest_framework import serializers
from manage_contact.models import contact_data, answer_data

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact_data
        fields = ['name', 'email', 'subject', 'message', 'ref_hash']

class ContactAnswer(serializers.ModelSerializer):
    class Meta:
        model = answer_data
        fields = ['user_name','answer','answer_to']
