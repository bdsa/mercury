from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from nexus.models import Contact

class ContactIndexView(generic.ListView):
    template_name = 'nexus/index.html'
    model = Contact

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactIndexView, self).dispatch(*args, **kwargs)
    
class ContactView(generic.DetailView):
    model = Contact
    template_name = 'nexus/contact_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactView, self).dispatch(*args, **kwargs)
