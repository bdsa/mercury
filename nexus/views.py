from django.shortcuts import render, get_object_or_404
from nexus.models import Contact

def index(request):
    contact_list = Contact.objects.all()
    context = {'contact_list': contact_list}
    return render(request, 'nexus/index.html', context)

def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    context = {'contact': contact}
    return render(request, 'nexus/contact_detail.html', context)

# Create your views here.
