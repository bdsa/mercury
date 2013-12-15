from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User, Group

from nexus.models import Contact

class ContactIndexView(generic.ListView):
    template_name = 'nexus/index.html'
    model = Contact

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(owner__in=user.groups.all())

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactIndexView, self).dispatch(*args, **kwargs)
    
class ContactView(generic.DetailView):
    model = Contact
    template_name = 'nexus/contact_detail.html'

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(owner__in=user.groups.all())

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactView, self).dispatch(*args, **kwargs)
