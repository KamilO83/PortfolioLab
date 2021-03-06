"""portfolio_projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from give_app.models import Institution
from give_app.views import LandingPageView, AddDonationView, LoginView, RegisterView, LogoutView, ProfilView, \
    FormCorfirmationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landingpage'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfilView.as_view(), name='profil'),
    path('form/', AddDonationView.as_view(), name='adddonation'),
    path('form/form-confirmation', FormCorfirmationView.as_view(), name='confirmation'),
    path('accounts/', include('django.contrib.auth.urls')),

]

