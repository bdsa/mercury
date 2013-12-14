from django.shortcuts import render, get_object_or_404
from django.views import generic
from nexus.models import Contact

class IndexView(generic.ListView):
    template_name = 'nexus/index.html'
    model = Contact
    
def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    context = {'contact': contact}
    return render(request, 'nexus/contact_detail.html', context)

# Create your views here.
