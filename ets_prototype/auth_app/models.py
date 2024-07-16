from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
import random
import string
    

def generate_admin_id():
    return "AD" + datetime.now().strftime("%Y%m%d%H%M%S") + ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
def generate_vendor_id():
    return "VE" + datetime.now().strftime("%Y%m%d%H%M%S") + ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
def generate_company_id():
    return "CO" + datetime.now().strftime("%Y%m%d%H%M%S") + ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
def generate_driver_id():
    return "DR" + datetime.now().strftime("%Y%m%d%H%M%S") + ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
def generate_employee_id():
    return "EM" + datetime.now().strftime("%Y%m%d%H%M%S") + ''.join(random.choice(string.ascii_uppercase) for _ in range(5))


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("vendor", "Vendor"),
        ("company", "Company"),
        ("driver", "Driver"),
        ("employee", "Employee"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class AdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    admin_id = models.CharField(max_length=20, default=generate_admin_id)
    phone = models.IntegerField(max_length=10)
    address = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the object.

        This method overrides the `__str__` method of the `CustomUser` class. It returns a string representation of the object by accessing the `username` attribute of the `user` attribute of the current instance.

        Returns:
            str: The username of the user associated with the current instance.
        """
        return self.user.username


class VendorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    vendor_id = models.CharField(max_length=20, default=generate_vendor_id)
    contact_person = models.CharField(max_length=50)
    contact_number = models.IntegerField(max_length=10)
    status = models.CharField(max_length=20, default="active", choices=(("active", "Active"), ("busy", "Busy"), ("inactive", "Inactive")))


class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_id = models.CharField(max_length=20, default=generate_company_id)
    contact_person = models.CharField(max_length=50)
    contact_number = models.IntegerField(max_length=10)

class DriverProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    driver_id = models.CharField(max_length=20, default=generate_driver_id)
    license_number = models.CharField(max_length=20)
    contact_number = models.IntegerField(max_length=10)
    status = models.CharField(max_length=20, default="active", choices=(("active", "Active"), ("busy", "Busy"), ("inactive", "Inactive")))


class EmployeeProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, default=generate_employee_id)
    contact_number = models.IntegerField(max_length=10)