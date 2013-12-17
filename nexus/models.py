from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.

class Contact(models.Model):
    forename = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    telephone_mobile = models.CharField("Mobile Telephone", max_length=25)
    roles = models.ManyToManyField('Role')
    owner = models.ForeignKey(Group)

    def _get_full_name(self):
        return '%s, %s' % (self.surname, self.forename)
    fullname = property(_get_full_name)

    def __unicode__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse('nexus:contact_detail', kwargs={'pk': self.pk})

class Role(models.Model):
    role = models.CharField(max_length=30)
    owner = models.ForeignKey(Group)

    def __unicode__(self):
        return self.role

    class Meta:
        unique_together = ('role', 'owner')
