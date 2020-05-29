from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
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
        if request.user.is_authenticated:
            form = DonationForm(request.POST)
            if form.is_valid():
                categories_all = Category.objects.all()
                donations = Donation.objects.all()
                institutions = Institution.objects.all()
                quantity = request.POST['quantity']
                categories = request.POST['categories']
                institution = request.POST['institution']
                adress = request.POST['adress']
                phone_number = request.POST['phone_number']
                city = request.POST['city']
                zip_code = request.POST['zip_code']
                pick_up_date = request.POST['pick_up_date']
                pick_up_time = request.POST['pick_up_time']
                pick_up_comment = request.POST['pick_up_comment']
                form = Donation.objects.create(quantity=quantity,
                                               categories=categories,
                                               institution=institution,
                                               adress=adress,
                                               phone_number=phone_number,
                                               city=city,
                                               zip_code=zip_code,
                                               pick_up_date=pick_up_date,
                                               pick_up_time=pick_up_time,
                                               pick_up_comment=pick_up_comment)
                form.save()
                if request.is_ajax():
                    return render(request, 'form.html', {'categories': categories_all,
                                                     'donations': donations,
                                                     'institutions': institutions,
                                                     'form':form})
            else:
                return redirect('/login/')

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


