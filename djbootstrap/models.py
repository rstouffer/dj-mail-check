from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField
from phone_field import PhoneField

# Create your models here.

class GUID(models.Model):
    guid = models.CharField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time = models.FloatField()

    def __str__(self):
        return self.user.username

class ExtraInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    company_name = models.CharField(max_length=100)

    address_l1 = models.CharField(max_length=100)
    address_l2 = models.CharField(max_length=100)

    city = models.CharField(max_length=100)
    state = USStateField()
    zip_code = models.CharField(max_length=5)

    phone = PhoneField()

    def __str__(self):
        return self.user.username