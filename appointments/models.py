from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
import datetime

service_field = \
    [('Actuators', 'Actuators'),
     ('Pipes and Valves', 'Pipes and Valves'),
     ('Pricing/Quotation', 'Pricing/Quotation'),
     ('Service and Repair', 'Service and Repair')]  # field for engineers


# Default user - deleted
def default_user():  # deleted users
    user = User(username="deleteduser", email="deleteduser@deleted.com")
    return user.id


# Admin
class Admin(models.Model):  # Admin details
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Admin")  # user foreign key
    image = models.ImageField(default="default.png", upload_to="profile_pictures")  # profile picture
    first_name = models.CharField(max_length=100, default='first_name')  # admin first name
    last_name = models.CharField(max_length=100, default='last_name')  # admin lastname
    dob = models.DateField(default=datetime.date.today)  # date of birth
    # contact?
    address = models.CharField(max_length=300, default="address")  # admin address
    city = models.CharField(max_length=100, default="city")  # admin city
    country = models.CharField(max_length=100, default="country")  # admin country
    postcode = models.IntegerField(default=0)  # admin postcode
    status = models.BooleanField(default=False)  # admin status (approved/on-hold)

    def __str__(self):
        return f'{self.admin.username} Admin Profile'


# Customer
class Customer(models.Model):  # customer details
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Customer")  # user foreign key
    image = models.ImageField(default="default.png", upload_to="profile_pictures", null=True,
                              blank=True)  # profile picture
    first_name = models.CharField(max_length=100, default='first_name')  # customer first name
    last_name = models.CharField(max_length=100, default='last_name')  # customer last name
    dob = models.DateField(default=datetime.date.today)  # customer date of birth
    company_name = models.CharField(max_length=300, default="company_name")  # customer address
    company_address = models.CharField(max_length=300, default="company_address")  # customer address
    # contact?
    city = models.CharField(max_length=100, default="city")  # customer city
    country = models.CharField(max_length=100, default="country")  # customer country
    postcode = models.IntegerField(default=0)  # customer postcode
    status = models.BooleanField(default=False)  # customer status (approved/on-hold)

    def __str__(self):
        return f'{self.customer.username} Customer Profile'


# Engineer
class Engineer(models.Model):  # engineer details
    engineer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Engineer")  # user foreign key
    image = models.ImageField(default="default.png", upload_to="profile_pictures")  # profile picture
    first_name = models.CharField(max_length=100, default='first_name')  # engineer firstname
    last_name = models.CharField(max_length=100, default='last_name')  # engineer lastname
    dob = models.DateField(default=datetime.date.today)  # engineer date of birth
    address = models.CharField(max_length=300, default="address")  # engineer address
    city = models.CharField(max_length=100, default="city")  # engineer city
    country = models.CharField(max_length=100, default="country")  # engineer country
    postcode = models.IntegerField(default=0)  # engineer postcode
    service_field = models.CharField(max_length=50, choices=service_field,
                                     default='Service and Repair')  # engineer service field from choices given as list
    status = models.BooleanField(default=False)  # engineer status(approved/on-hold)

    def __str__(self):
        return f'{self.engineer.username} Engineer Profile'


# Engineer service field
class EngineerServiceField(models.Model):
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, related_name="EngineerServiceField")  # engineer fk
    app_total = models.IntegerField(default=0)  # total customers/appointments completed by engineer

    def __str__(self):
        return f'{self.engineer.first_name} Service Field Information'


# Appointment
class Appointment(models.Model):  # customer appointment details
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="CustomerApp")  # customer fk
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, related_name="EngineerApp")  # engineer fk
    description = models.TextField(max_length=500)  # appointment description
    app_link = models.TextField(null=True, blank=True)  # video call room link
    app_date = models.DateField(null=True, blank=True)  # call date
    app_time = models.TimeField(null=True, blank=True)  # call time/slot
    status = models.BooleanField(default=False)  # appointment status (approved/on-hold)
    completed = models.BooleanField(default=False)  # appointment completed/to-be-done
    # approval_date = models.DateField(null=True, blank=True)  # date appointment approved
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.description} Appointment Information'


# Appointment rating
class AppointmentRating(models.Model):
    rating = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(0)])

    def __str__(self):
        return f'{self.rating} Stars - Appointment Rating Information'


# Approved appointment
class ApprovedCustomerAppointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="CustomerApprovedApp")  # customer fk
    engineer = models.ForeignKey(Engineer, on_delete=models.CASCADE, related_name="EngineerApprovedApp")  # engineer fk
    approval_date = models.DateField()  # date appointment approved
    description = models.TextField()  # appointment description
    completed_date = models.DateField(null=True, blank=True)  # date of completed appointment

    def __str__(self):
        return f'{self.customer} Approved Appointment Information'
