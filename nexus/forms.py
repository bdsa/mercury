#from django import forms
import floppyforms as forms

from nexus.models import Contact, Role, Event, Booking, Programme

class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('request_user') 
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['roles'].queryset = Role.objects.filter(owner=user.groups.all()[0])

    telephone_mobile = forms.RegexField(label=('Mobile Telephone'), max_length=25, regex=r'^[\+]?\d{2}(?: ?\d+)*$', error_message=("Please enter a valid phone number."),)

    class Meta:
        model = Contact
        exclude = ('owner',)

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('request_user') 
        super(RoleForm, self).__init__(*args, **kwargs)
        self.fields['owner'].queryset = user.groups.all()

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('request_user') 
        super(EventForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.cleaned_data.get('startdate') > self.cleaned_data.get('enddate'):
            raise forms.ValidationError("The event's start date must be earlier than its end.")
        return self.cleaned_data

class BookingCreateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('role',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('request_user') 
        super(BookingCreateForm, self).__init__(*args, **kwargs)
        self.fields['role'].queryset = Role.objects.filter(owner=user.groups.all()[0])

class BookingUpdateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('contact',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('request_user') 
        super(BookingUpdateForm, self).__init__(*args, **kwargs)
        self.fields['contact'].queryset = Contact.objects.filter(owner=user.groups.all()[0], roles=self.instance.role.id)

    def clean(self):
        newbookingstartdate = self.instance.event.startdate
        newbookingenddate =  self.instance.event.enddate
        contact = self.cleaned_data.get('contact')

        if contact:
            for booking in contact.booking_set.all():
                if (booking.event.startdate < newbookingstartdate < booking.event.enddate) or (booking.event.startdate < newbookingenddate < booking.event.enddate):
                    raise forms.ValidationError("This booking conflicts with another for the same contact: %(ebooking)s" % {'ebooking': booking.event})
        return self.cleaned_data

class BookingDeleteForm(forms.ModelForm):
    class Meta:
        model = Booking

class ProgrammeForm(forms.ModelForm):
    class Meta:
        model = Programme
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('request_user') 
        super(ProgrammeForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.cleaned_data.get('deliverydate') > self.cleaned_data.get('transmissiondate'):
            raise forms.ValidationError("The programme's transmission date cannot be before its delivery date.")
        return self.cleaned_data
