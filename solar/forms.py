from django import forms
from solar.models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = '__all__'
