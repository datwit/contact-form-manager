from django.shortcuts import render, redirect 
from django.core.mail import send_mail, get_connection
from .forms import ContactForm
from .models import ContactData

# Create your views here.

def contact(request):
	form= ContactForm(request.POST or None)
	contact= False
	if form.is_valid():
		new_contact= form.save()
		contact = True
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
	
	context= {'form': form , 'contacted': contact}
	return render(request, 'manager/contact.html', context)

def data(request, contactID):
	element=ContactData.objects.get(ref_hash= contactID)
	context={'element': element}
	return render(request, 'manager/data.html', context)
