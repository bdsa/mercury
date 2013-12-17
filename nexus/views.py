from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy

from nexus.forms import ContactForm, RoleForm
from nexus.models import Contact, Role

class LoginRequiredMixin(object):
    # Require user to be logged in to see this view
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class AutoOwnerMixin(object):
    # Use this mixin to automatically set 'owner' to the user's first group
    def form_valid(self, form):
        form.instance.owner = self.request.user.groups.all()[0]
        return super(AutoOwnerMixin, self).form_valid(form)

class ContactIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'nexus/index.html'
    model = Contact

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(owner__in=user.groups.all())

class ContactView(LoginRequiredMixin, generic.DetailView):
    model = Contact
    template_name = 'nexus/contact_detail.html'

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(owner__in=user.groups.all())

class ContactCreate(LoginRequiredMixin, AutoOwnerMixin, generic.CreateView):
    model = Contact
    form_class = ContactForm

    # pass request user to form to filter role choices
    def get_form_kwargs(self):
        kwargs = super(ContactCreate, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        return kwargs

class ContactUpdate(LoginRequiredMixin, AutoOwnerMixin, generic.UpdateView):
    model = Contact
    form_class = ContactForm

    # pass request user to form to filter role choices
    def get_form_kwargs(self):
        kwargs = super(ContactUpdate, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        return kwargs

class ContactDelete(LoginRequiredMixin, generic.DeleteView):
    model = Contact
    form_class = ContactForm

class RoleIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'nexus/role_index.html'
    model = Role

    def get_queryset(self):
        user = self.request.user
        return Role.objects.filter(owner__in=user.groups.all())

class RoleCreate(LoginRequiredMixin, AutoOwnerMixin, generic.CreateView):
    model = Role
    form_class = RoleForm

    # pass request user to form to filter owner choices
    def get_form_kwargs(self):
        kwargs = super(RoleCreate, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        return kwargs
