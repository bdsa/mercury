from django.shortcuts import render, get_object_or_404, render_to_response
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django import forms

from nexus.forms import ContactForm, RoleForm, EventForm, BookingCreateForm, BookingUpdateForm, BookingDeleteForm, ProgrammeForm
from nexus.models import Contact, Role, Event, Booking, Programme

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

class RoleDelete(LoginRequiredMixin, generic.DeleteView):
    model = Role
    form_class = RoleForm

class EventIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'nexus/event_index.html'
    model = Event

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(owner__in=user.groups.all())

class EventView(LoginRequiredMixin, generic.DetailView):
    model = Event
    template_name = 'nexus/event_detail.html'

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(owner__in=user.groups.all())

class EventUpdate(LoginRequiredMixin, AutoOwnerMixin, generic.UpdateView):
    model = Event
    form_class = EventForm

    # pass request user to form to filter role choices
    def get_form_kwargs(self):
        kwargs = super(EventUpdate, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        return kwargs

class EventCreate(LoginRequiredMixin, AutoOwnerMixin, generic.CreateView):
    model = Event
    form_class = EventForm

    # pass request user to form to filter role choices
    def get_form_kwargs(self):
        kwargs = super(EventCreate, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        return kwargs

class EventDelete(LoginRequiredMixin, generic.DeleteView):
    model = Event
    form_class = EventForm

class BookingCreate(LoginRequiredMixin, AutoOwnerMixin, generic.CreateView):
    model = Booking
    form_class = BookingCreateForm

    # pass request user to form to filter role choices
    def get_form_kwargs(self):
        kwargs = super(BookingCreate, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.event = Event.objects.get(id=self.kwargs['event_id'])
        form.instance.owner = self.request.user.groups.all()[0]
        return super(BookingCreate, self).form_valid(form)

class BookingUpdate(LoginRequiredMixin, AutoOwnerMixin, generic.UpdateView):
    model = Booking
    form_class = BookingUpdateForm

    # pass request user to form to filter role choices
    def get_form_kwargs(self):
        kwargs = super(BookingUpdate, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.event = Event.objects.get(id=self.kwargs['event_id'])
        form.instance.owner = self.request.user.groups.all()[0]
        return super(BookingUpdate, self).form_valid(form)

class BookingDelete(LoginRequiredMixin, generic.DeleteView):
    model = Booking
    form_class = BookingDeleteForm

    def get_success_url(self):
        return reverse('nexus:event_detail', kwargs = {'pk': self.object.event.id},)

class ProgrammeIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'nexus/programme_index.html'
    model = Programme

    def get_queryset(self):
        user = self.request.user
        return Programme.objects.filter(owner__in=user.groups.all())

class ProgrammeCreate(LoginRequiredMixin, AutoOwnerMixin, generic.CreateView):
    model = Programme
    form_class = ProgrammeForm

    # pass request user to form to filter role choices
    def get_form_kwargs(self):
        kwargs = super(ProgrammeCreate, self).get_form_kwargs()
        kwargs.update({'request_user': self.request.user})
        return kwargs

class ProgrammeView(LoginRequiredMixin, generic.DetailView):
    model = Programme
    template_name = 'nexus/programme_detail.html'

    def get_queryset(self):
        user = self.request.user
        return Programme.objects.filter(owner__in=user.groups.all())
