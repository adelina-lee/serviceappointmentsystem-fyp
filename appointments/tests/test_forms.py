from django.test import TestCase
from appointments.forms import AdminRegistrationForm, AdminUpdateForm, AdminAppointmentForm, \
    CustomerRegistrationForm, CustomerUpdateForm, CustomerAppointmentForm, EngineerRegistrationForm, \
    EngineerUpdateForm, FeedbackForm
from django.utils import timezone
from datetime import date, timedelta, time
from appointments.models import User, Admin, Customer, Engineer, EngineerServiceField, Appointment


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

    admin = Admin(admin=new_user,  # Admin
                  first_name='first_name',
                  last_name='last_name',
                  dob=dt,
                  address='address',
                  city='city',
                  country='country',
                  postcode=12345)

    def test_engineer_update_invalid(self):  # Invalid engineer details
        dt = timezone.now().date()
        form = EngineerUpdateForm(data={
            "first_name": "first name",
            "last_name": "last name",
            "dob": dt,
            "address": "test address",
            "country": "test country",
            "city": "test city",
            "postcode": "postcode",
        })
        # print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_customer_update_invalid(self):  # Invalid customer details
        dt = timezone.now().date()
        form = CustomerUpdateForm(data={
            "first_name": "first name",
            "last_name": "last name",
            "dob": dt,
            "company_name": "test company name",
            "company_address": "test address",
            "country": "test country",
            "city": "test city",
            "postcode": "postcode",
        })
        # print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_customer_appointment_form_invalid(self):  # Invalid customer appointment form
        dt = date(12, 12, 12)
        self.new_user.save()
        self.engineer.save()
        self.customer.save()
        form = CustomerAppointmentForm(
            data={
                'engineer': self.engineer,
                'app_date': dt,
                'app_time': "9:00 AM",
                'description': "test description"
            })
        # print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_admin_appointment_form_invalid(self):  # Invalid admin appointment form
        dt = date(12, 12, 12)
        self.new_user.save()
        self.engineer.save()
        self.customer.save()
        form = AdminAppointmentForm(
            data={
                'engineer': self.engineer,
                'customer': self.customer,
                'app_date': dt,
                'app_time': "9:00 AM",
                'description': "test description"
            })
        # print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
