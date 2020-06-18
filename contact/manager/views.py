from django.shortcuts import render, redirect 
from .forms import ContactForm
from .models import ContactData

# Create your views here.


def contact(request):
	form= ContactForm(request.POST or None)
	if form.is_valid():
		new_contact= form.save()
		#create advise email with data
		return redirect('data/' + str(new_contact.ref_number))
	context= {'form': form }
	return render(request, 'manager/contact.html', context)

def data(request, contactID):
	element=ContactData.objects.get(ref_number= contactID)
	context={'element': element}
	return render(request, 'manager/data.html', context)
