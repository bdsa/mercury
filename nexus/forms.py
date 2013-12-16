from django import forms
from nexus.models import Contact, Role

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
        exclude = ('owner',)
