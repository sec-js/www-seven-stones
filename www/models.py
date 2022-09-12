from __future__ import unicode_literals

from django.db import models
from django import forms
from captcha.fields import CaptchaField

# Create your models here.

class Contacts(models.Model):
    name = models.CharField('Name', max_length=40)
    email = models.CharField('Email address', max_length=40)
    mobile = models.CharField('Mobile number', max_length=30)
    message = models.CharField('Message', max_length=300)
    ip_address = models.CharField('ip_address', max_length=20, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u'%s : %s' % (self.name, self.email)


class ContactForm(forms.Form):

    name = forms.CharField(label='Name', max_length=60, required=True,
                           widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='Email', required=True,
                             widget=forms.TextInput(attrs={'class': "form-control"}))
    message = forms.CharField(label='Message', max_length=600, required=True,
                              widget=forms.Textarea(attrs={'class': "form-control"}))
    captcha = CaptchaField()

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        message = cleaned_data.get("message")

        return cleaned_data