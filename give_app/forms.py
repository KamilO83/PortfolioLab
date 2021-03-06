from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from give_app.models import Donation


class RegistrationForm(forms.Form):

    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Imię'}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'placeholder':'Nazwisko'}))
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'placeholder':'Hasło'}),
                               )
    re_password = forms.CharField(label='',
                                  widget=forms.PasswordInput(attrs={'placeholder':'Powtórz hasło'}))

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['re_password']:
                raise ValidationError("Hasła nie są identyczne")
        return self.cleaned_data


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        exclude = ('user', 'institution', 'categories')