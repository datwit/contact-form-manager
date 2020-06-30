from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.core.mail import send_mail, get_connection
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from manageContact.models import ContactData
from manageContact.serializers import ContactSerializer

@csrf_exempt
def Contact_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            new_contact= serializer.save()

            con = get_connection('django.core.mail.backends.console.EmailBackend')
		
            content='Name: ' + new_contact.name + '\nEmail: '+ new_contact.email + '\nSubject: ' + new_contact.subject + '\nMessage: ' + new_contact.message 
                
            #create advise email to enterprise
            send_mail(
                'New user contact',
                content + '\nLink to access: http://datwit.com/contact/data/' + str(new_contact.ref_hash),
                'noreply@gmail.com',
                ['siteowner@example.com'],
                connection=con,
                )
                
            #create advise email to user
            send_mail(
                'New user contact',
                content,
                'noreply@gmail.com',
                ['siteowner@example.com'],
                connection=con,
                )

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def contact_detail(request, contactID):
    """
    Retrieve, update or delete a code snippet.
    """
    if contactID == "all":
        contact = ContactData.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        try:
            contact = ContactData.objects.get(ref_hash= contactID)
        except contact.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = ContactSerializer(contact)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ContactSerializer(contact, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            contact.delete()
            return HttpResponse(status=204)