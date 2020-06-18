from django.shortcuts import render, redirect 
from django.core.mail import send_mail, get_connection
from .forms import ContactForm
from .models import ContactData

# Create your views here.


def contact(request):
	form= ContactForm(request.POST or None)
	if form.is_valid():
		new_contact= form.save()
		#create advise email with data
		con = get_connection('django.core.mail.backends.console.EmailBackend')
		send_mail(
			'New user contact',
			'Name: ' + new_contact.name + '\nEmail: '+ new_contact.email + 
			'\nSubject: ' + new_contact.subject + '\nMessage: ' + new_contact.message + 
			'\nLink to access: http://datwit.com/contact/data/' + str(new_contact.ref_number),
			'noreply@gmail.com',
			['siteowner@example.com'],
			connection=con,
			)
		return redirect('data/' + str(new_contact.ref_number))
	context= {'form': form }
	return render(request, 'manager/contact.html', context)

def data(request, contactID):
	element=ContactData.objects.get(ref_number= contactID)
	context={'element': element}
	return render(request, 'manager/data.html', context)
