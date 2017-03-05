from django.forms import ModelForm
from django.contrib.auth.models import User
from homeSense.models import EmergencyContact


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


# class EmergencyContactForm(ModelForm):
#     class Meta:
#         model = EmergencyContact
#         fields = ('first_name', 'last_name', 'phone', 'email', )