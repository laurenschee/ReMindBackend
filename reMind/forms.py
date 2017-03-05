from django import forms
from .models import EmergencyContact


class EmergencyContactForm(forms.Form):
    first_name = forms.CharField(label='Your First Name', max_length=100)
    last_name = forms.CharField(label='Your Last Name', max_length=100)
    phone = forms.CharField(label='Phone Number', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    home_name = forms.CharField(label='Home Name', max_length=100)