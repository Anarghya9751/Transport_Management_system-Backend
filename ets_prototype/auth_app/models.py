from django.contrib.auth.models import AbstractUser
from django.db import models

from datetime import datetime
import random
import string

from utils.useful_functions import generate_id


def generate_admin_id():
    return "AD" + generate_id()


def generate_commander_id():
    return "CM" + generate_id()


def generate_vendor_id():
    return "VE" + generate_id()


def generate_company_id():
    return "CO" + generate_id()


def generate_driver_id():
    return "DR" + generate_id()


def generate_employee_id():
    return "EM" + generate_id()


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("commander", "Commander"),
        ("vendor", "Vendor"),
        ("company", "Company"),
        ("driver", "Driver"),
        ("employee", "Employee"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


class AdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    admin_id = models.CharField(max_length=20, default=generate_admin_id)
    contact_number = models.IntegerField()
    address = models.TextField()
    aadhar_number = models.IntegerField()

    def __str__(self):
        """
        Returns a string representation of the object.

        This method overrides the `__str__` method of the `CustomUser` class. It returns a string representation of the object by accessing the `username` attribute of the `user` attribute of the current instance.

        Returns:
            str: The username of the user associated with the current instance.
        """
        return self.admin_id


class CommanderProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    commander_id = models.CharField(max_length=20, default=generate_commander_id)
    contact_number = models.IntegerField()
    address = models.TextField()
    status = models.CharField(
        max_length=20,
        default="active",
        choices=(("active", "Active"), ("inactive", "Inactive")),
    )
    aadhar_number = models.IntegerField()

    def __str__(self):
        return self.commander_id


class VendorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    vendor_id = models.CharField(max_length=20, default=generate_vendor_id)
    contact_person = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    address = models.TextField()
    status = models.CharField(
        max_length=20,
        default="active",
        choices=(("active", "Active"), ("busy", "Busy"), ("inactive", "Inactive")),
    )
    aadhar_number = models.IntegerField()

    def __str__(self):
        return self.vendor_id


class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_id = models.CharField(max_length=20, default=generate_company_id)
    contact_person = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    address = models.TextField()
    aadhar_number = models.IntegerField()

    def __str__(self):
        return self.company_id


class DriverProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    driver_id = models.CharField(max_length=20, default=generate_driver_id)
    license_number = models.CharField(max_length=20)
    contact_number = models.IntegerField()
    address = models.TextField()
    status = models.CharField(
        max_length=20,
        default="active",
        choices=(("active", "Active"), ("busy", "Busy"), ("inactive", "Inactive")),
    )
    aadhar_number = models.IntegerField()

    def __str__(self):
        return self.driver_id


class EmployeeProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, default=generate_employee_id)
    contact_number = models.IntegerField()
    address = models.TextField()
    aadhar_number = models.IntegerField()
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()

    def __str__(self):
        return self.employee_id
