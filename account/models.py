from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class DeviceDetail(models.Model):
    device_id = models.CharField(max_length=100)
    device_token = models.CharField(max_length=100)


class UserDetail(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(DeviceDetail, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    phone_country_code = models.CharField(max_length=4)
    address = models.TextField()
    otp = models.IntegerField()