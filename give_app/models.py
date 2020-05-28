from django.conf import settings
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Institution(models.Model):
    FUNDACJA = 'FUN'
    ORGANIZACJA = 'OP'
    ZBIORKA = 'ZL'
    TYPE_CHOOICES = [
        (FUNDACJA, "fundacja"),
        (ORGANIZACJA, "organizacja pozarządowa"),
        (ZBIORKA, "zbiórka lokalna"),
    ]
    name = models.CharField(max_length=40)
    type = models.PositiveIntegerField(choices=TYPE_CHOOICES, default=FUNDACJA)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    adress = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=36)
    zip_code = models.IntegerField()
    pick_up_date = models.DateField
    pick_up_time = models.DateTimeField
    pick_up_comment = models.TextField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
