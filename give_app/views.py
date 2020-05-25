from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
from give_app.forms import RegistrationForm
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
        form = RegistrationForm()
        return render(request, 'register.html', {'form':form})

    def post (self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = password
            form = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                            password=password, username=email)
            form.save()
            return render(request,'register.html', {'form': form} )
        return render(request,'login.html')



