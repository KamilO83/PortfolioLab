from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
from give_app.forms import RegistrationForm, DonationForm
from give_app.models import Donation, Institution, Category


class LandingPageView(View):
    def get(self, request):
        donations = Donation.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'index.html', {'donations':donations,
                                              'institutions':institutions})

class AddDonationView(View):
    def get(self, request):
        if request.user.is_authenticated:
            categories_all = Category.objects.all()
            donations = Donation.objects.all()
            institutions = Institution.objects.all()
            return render(request, 'form.html', {'categories':categories_all,
                                                 'donations':donations,
                                                 'institutions':institutions})
        else:
            return redirect('/login/')

    def post(self, request):
        if request.is_ajax():
            form = DonationForm(request.POST)
            if form.is_valid():
                instance = form.save()
                ser_instance = serializers.serialize('json', [instance])
                return JsonResponse({"instance":ser_instance}, status=200)
            else:
                return JsonResponse({"error": form.errors}, status=400)


class FormCorfirmationView(View):
    # def get(self,request):
    #     return render(request, 'form-confirmation.html')

    def post(self,request):
        return render(request, 'form-confirmation.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/register")


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("/")


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
            return render(request,'login.html', {'form': form} )
        return render(request,'register.html')

class ProfilView(View):
    def get(self,request):
        return render(request, 'profil.html')


