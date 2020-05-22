from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
from give_app.forms import SignUpForm
from give_app.models import Donation, Institution



class LandingPageView(View):
    def get(self, request):
        donation_quantity = Donation.objects.all()
        # institution_id = Institution.objects.latest(id) 'institutions':institution_id
        return render(request, 'index.html', {'donations':donation_quantity,})

class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    # def post (self, request):
