from django import forms

from .models import Customer


class CustomerRegisterForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'login', 'password')


class CustomerLoginForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('login', 'password')
