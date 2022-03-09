from django.test import TestCase
from appointments.forms import AdminRegistrationForm, AdminUpdateForm, AdminAppointmentForm, \
    CustomerRegistrationForm, CustomerUpdateForm, CustomerAppointmentForm, EngineerRegistrationForm, \
    EngineerUpdateForm, FeedbackForm
from django.utils import timezone
from datetime import date, timedelta, time
from appointments.models import User, Admin, Customer, Engineer, EngineerServiceField, Appointment, \
    ApprovedCustomerAppointment


class FormTest(TestCase):
    new_user = User(username='username', email='email@gmail.com', password='password1')  # New user
    dt = timezone.now().date()  # Timezone

    engineer = Engineer(engineer=new_user,  # Engineer
                        first_name='first_name',
                        last_name='last_name',
                        service_field='service_field',
                        dob=dt,
                        address='address',
                        city='city',
                        country='country',
                        postcode=12345)

    customer = Customer(customer=new_user,  # Customer
                        first_name='first_name',
                        last_name='last_name',
                        dob=dt,
                        company_name='company_name',
                        company_address='company_address',
                        city='city',
                        country='country',
                        postcode=12345)

    def test_appointment_create(self):  # Create appointment test
        dt = timezone.now().date()
        tm = timezone.now().time()
        self.new_user.save()
        self.engineer.save()
        self.customer.save()
        app = Appointment.objects.create(engineer=self.engineer,
                                         customer=self.customer,
                                         app_date=dt,
                                         app_time=tm,
                                         description="Testing Appointment Creation")
        self.assertEquals(str(app), "Testing Appointment Creation Appointment Information")

    def test_approve_appointment(self):  # Approved appointment test
        dt = timezone.now().date()
        self.new_user.save()
        self.engineer.save()
        self.customer.save()
        approved_app = ApprovedCustomerAppointment(engineer=self.engineer,
                                                   customer=self.customer,
                                                   approval_date=dt,
                                                   description="username Customer Profile Approved Appointment Creation")
        self.assertEquals(str(approved_app), "username Customer Profile Approved Appointment Information")

    def test_engineer_service_field(self):
        self.new_user.save()
        self.engineer.save()
        service_field = EngineerServiceField(engineer=self.engineer,
                                             app_total=0)
        self.assertEquals(str(service_field), "first_name Service Field Information")
