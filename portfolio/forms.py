# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Contact
from django import forms

class ContactForm(ModelForm):
    """
    Contact form for the contact page.
    """
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
          'message': forms.Textarea(attrs={'rows':2}),
        }