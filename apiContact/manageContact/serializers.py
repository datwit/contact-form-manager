from django.contrib.auth.models import User, Group
from rest_framework import serializers
from manageContact.models import ContactData


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactData
        fields = ['name', 'email', 'subject', 'message']

"""
class ContactSerializer(serializers.Serializer):
	email= serializers.EmailField()
	name= serializers.CharField(max_length=100)
	subject= serializers.CharField(max_length=200)
	message= serializers.CharField(max_length=10000)
	attended= serializers.BooleanField(default= False)
	
	def create(self, validated_data):
		""""""
		Create and return a new `Contact` instance, given the validated data.
		""""""
		return ContactData.objects.create(**validated_data)
	
	def update(self, instance, validated_data):
		""""""
		Update and return an existing `Contact` instance, given the validated data.
		""""""
		instance.message = validated_data.get('title', instance.title)
		instance.attended = validated_data.get('code', instance.code)
		instance.save()
		return instance
"""