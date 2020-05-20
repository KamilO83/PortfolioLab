from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView


class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'signUp.html'

