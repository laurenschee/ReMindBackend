from django import forms
from django.contrib.auth.models import User
from reMind.models import Home, Sensor, EmergencyContact


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


# class HomeForm(forms.ModelForm):
#     home_name = forms.CharField()
#
#     def save(self, commit=True):
#         home_name = self.cleaned_data.get('home_name', None)
#         self.instance.nickname = home_name
#         self.instance.save()
#         return super(HomeForm, self).save(commit=commit)
#
#     class Meta:
#         model = Home
#         fields = ('owner', 'home_name')