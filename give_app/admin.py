from django.contrib import admin
from .models import Institution
# Register your models here.
class InstitutionAdmin:
    model = Institution

admin.site.register(Institution)