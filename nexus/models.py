from django.db import models

# Create your models here.
class Contact(models.Model):
    forename = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    telephone_mobile = models.CharField("Mobile Telephone", max_length=14)

    def _get_full_name(self):
        return '%s, %s' % (self.surname, self.forename)
    fullname = property(_get_full_name)

    def __unicode__(self):
        return self.fullname

class Role(models.Model):
    role = models.CharField(max_length=30)
    contacts = models.ManyToManyField(Contact, blank=True)

    def __unicode__(self):
        return self.role
