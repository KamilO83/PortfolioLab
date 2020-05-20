from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

# Create your models here.
TYPE_CHOOICES = (
    ("1", "fundacja"),
    ("2", "organizacja pozarządowa"),
    ("3", "zbiórka lokalna"),
)
class Category(models.Model):
    name = models.CharField(max_length=16)

class Institution(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=20, choices=TYPE_CHOOICES, default="1")
    categories = models.ManyToManyField(Category)

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    adress = models.CharField(max_length=128)
    phone_number = models.IntegerField(max_length=12)
    city = models.CharField(max_length=36)
    zip_code = models.IntegerField(max_length=6)
    pick_up_date = models.DateField
    pick_up_time = models.DateTimeField
    pick_up_comment = models.TextField(max_length=300)
    user = models.ForeignKey(AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)