from django.shortcuts import render, get_object_or_404
from django.views import generic
from nexus.models import Contact

class ContactIndexView(generic.ListView):
    template_name = 'nexus/index.html'
    model = Contact
    
class ContactView(generic.DetailView):
    model = Contact
    template_name = 'nexus/contact_detail.html'
