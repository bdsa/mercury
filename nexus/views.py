from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

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

class ContactCreate(generic.CreateView):
    model = Contact
    fields = ['forename', 'surname', 'telephone_mobile', 'email']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user.groups.all()[0]
        return super(ContactCreate, self).form_valid(form)
