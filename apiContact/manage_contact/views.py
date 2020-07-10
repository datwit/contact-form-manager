import uuid
from rest_framework import viewsets
from django.core.mail import send_mail, get_connection
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from manage_contact.models import contact_data
from manage_contact.serializers import ContactSerializer, ContactAnswer

@csrf_exempt
def create_contact(request):
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
                content + '\nLink to access: http://localhost:8000/contact/data/' + str(new_contact.ref_hash),
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

            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def contact_detail(request, ref_hash):
    """
    Retrieve, update or delete a code snippet.
    """
    if ref_hash == "all":
        contact = contact_data.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        try:
            contact = contact_data.objects.get(ref_hash = ref_hash)
        except contact.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET' and contact.active==True:
            contacts=contact_data.objects.filter( email = contact.email)    
            serializer = ContactSerializer(contacts, many=True)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer_answer = ContactAnswer(data=data)
            serializer_answer.answer_to = contact.id
            if serializer_answer.is_valid():
                serializer_answer.save()
                contact.ref_hash = uuid.uuid4()
                contact.save()

                return JsonResponse(serializer_answer.data)
            return JsonResponse(serializer_answer.errors, status=400)

        elif request.method == 'DELETE':
            contact.active = False
            contact.ref_hash = uuid.uuid4()
            contact.save()
            return HttpResponse(status=204)

        else:
            return HttpResponse(status=404)