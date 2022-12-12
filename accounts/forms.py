from django_registration.forms import RegistrationForm
from django import forms

from accounts.models import User


class CustomUserForm(RegistrationForm):
    email = forms.EmailField(label='email')
    first_name = forms.CharField(max_length=50, label='first_name')
    last_name = forms.CharField(max_length=50, label='last_name')

    class Meta(RegistrationForm.Meta):
        model = User
        fields = ['email','first_name', 'last_name']
