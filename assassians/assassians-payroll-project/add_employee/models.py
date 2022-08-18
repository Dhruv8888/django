from django.db import models

# Create your models here.
class device(models.Model):
    Id = models.CharField(max_length=17, primary_key=True, unique=True)
    # macId = models.CharField(max_length=17, primary_key=True, unique=True)
    DeviceType = models.CharField(max_length=20)
    DeviceVersion = models.CharField(max_length=20)
    DeviceLocation = models.CharField(max_length=50)
    # we want this field as nullable can be null  , NotRequired=True
    PrimaryGroup = models.CharField(max_length=50)
    # we want this field as nullable can be null  , NotRequired=True
    SecondaryGroup = models.CharField(max_length=50)
    RegistrationTime = models.CharField(max_length=50)
    LastContact = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    Status = models.CharField(max_length=4, null=True)


# class device_last_updated:
#     macId = models.CharField(max_length=17, fore=True, unique=True)
#     last_contacted(datetime)
