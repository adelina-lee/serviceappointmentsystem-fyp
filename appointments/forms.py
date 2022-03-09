from django import forms
from django.contrib.auth.models import User

from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime
from django.forms.widgets import SelectDateWidget
from django.utils import timezone

from .models import Admin, Customer, Engineer, Appointment, ApprovedCustomerAppointment

service_field = \
    [('Actuators', 'Actuators'),
     ('Pipes and Valves', 'Pipes and Valves'),
     ('Pricing/Quotation', 'Pricing/Quotation'),
     ('Service and Repair', 'Service and Repair')]  # field for engineers


# Admin registration form
class AdminRegistrationForm(UserCreationForm):  # to register an admin
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    username.widget.attrs.update({'class': 'app-form-control'})

    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    email.widget.attrs.update({'class': 'app-form-control'})

    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    first_name.widget.attrs.update({'class': 'app-form-control'})

    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    last_name.widget.attrs.update({'class': 'app-form-control'})

    dob = forms.DateField(label="", widget=SelectDateWidget(years=range(1960, 2021)))
    dob.widget.attrs.update({'class': 'app-form-control-date'})

    address = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your address'}))
    address.widget.attrs.update({'class': 'app-form-control'})

    city = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'City'}))
    city.widget.attrs.update({'class': 'app-form-control'})

    country = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    country.widget.attrs.update({'class': 'app-form-control'})

    postcode = forms.IntegerField(label="", widget=forms.TextInput(attrs={'placeholder': 'Postcode'}))
    postcode.widget.attrs.update({'class': 'app-form-control'})

    image = forms.ImageField(label="")
    image.widget.attrs.update({'class': 'app-form-control'})

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password1.widget.attrs.update({'class': 'app-form-control'})

    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again'}))
    password2.widget.attrs.update({'class': 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'dob', 'address', 'city', 'country', 'postcode',
                  'image', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


# Admin details update form
class AdminUpdateForm(forms.ModelForm):  # used to edit an admin instance
    first_name = forms.CharField()
    last_name = forms.CharField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2022)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Admin
        fields = ['first_name', 'last_name', 'dob', 'address', 'city', 'country', 'postcode', 'image']


# Admin appointment form
class AdminAppointmentForm(forms.ModelForm):  # book an appointment by admin
    engineer = forms.TypedChoiceField(label='')  # engineer is chosen from existing engineers in db
    engineer.widget.attrs.update({'class': 'app-form-control'})
    customer = forms.TypedChoiceField(label='')  # customer is chosen from existing customers in db
    customer.widget.attrs.update({'class': 'app-form-control'})
    app_date = forms.DateField(label='', widget=SelectDateWidget(years=range(2022, 2024)))  # appointment date
    app_date.widget.attrs.update({'class': 'app-form-control-date'})
    app_time = forms.TypedChoiceField(label='')  # time of appointment
    app_time.widget.attrs.update({'class': 'app-form-control'})
    description = forms.CharField(max_length=300, label='',
                                  widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    description.widget.attrs.update({'class': 'app-form-control'})

    def __init__(self, *args, **kwargs):
        super(AdminAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['engineer'].choices = [(c.id, c.first_name + " " + c.last_name + " (" + c.service_field + ")")
                                           for c in Engineer.objects.filter(status=True).all()]
        # choose engineers from db
        self.fields['customer'].choices = [(c.id, c.first_name + " " + c.last_name + " (" + c.company_name + ")")
                                           for c in Customer.objects.filter(status=True).all()]
        # choose customers from db
        self.fields['app_time'].choices = [('9:00 AM', '9:00 AM'), ('10:00 AM', '10:00 AM'), ('11:00 AM', '11:00 AM'),
                                           ('13:00 PM', '13:00 PM'), ('14:00 PM', '14:00 PM'), ('15:00 PM', '15:00 PM'),
                                           ('16:00 PM', '16:00 PM'), ('17:00 PM', '17:00 PM')]
        # choices for time slot for appointment

    class Meta:
        model = Appointment
        fields = ['description', 'app_date', 'app_time']


# Customer registration form
class CustomerRegistrationForm(UserCreationForm):  # register customer
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    username.widget.attrs.update({'class': 'app-form-control'})

    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    email.widget.attrs.update({'class': 'app-form-control'})

    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    first_name.widget.attrs.update({'class': 'app-form-control'})

    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    last_name.widget.attrs.update({'class': 'app-form-control'})

    dob = forms.DateField(label="", widget=SelectDateWidget(years=range(1960, 2022)))
    dob.widget.attrs.update({'class': 'app-form-control-date'})

    company_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your company name'}))
    company_name.widget.attrs.update({'class': 'app-form-control'})

    company_address = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your company address'}))
    company_address.widget.attrs.update({'class': 'app-form-control'})

    city = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'City'}))
    city.widget.attrs.update({'class': 'app-form-control'})

    country = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    country.widget.attrs.update({'class': 'app-form-control'})

    postcode = forms.IntegerField(label="", widget=forms.TextInput(attrs={'placeholder': 'Postcode'}))
    postcode.widget.attrs.update({'class': 'app-form-control'})

    image = forms.ImageField(label="")
    image.widget.attrs.update({'class': 'app-form-control'})

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password1.widget.attrs.update({'class': 'app-form-control'})

    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again'}))
    password2.widget.attrs.update({'class': 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'dob', 'company_name', 'company_address',
                  'city', 'country', 'postcode', 'image', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


# Customer update form
class CustomerUpdateForm(forms.ModelForm):  # update customer details
    first_name = forms.CharField()
    last_name = forms.CharField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2022)))
    company_name = forms.CharField()
    company_address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'dob', 'company_name', 'company_address', 'city', 'country', 'postcode',
                  'image']


# Customer appointment form
class CustomerAppointmentForm(forms.ModelForm):  # make an appointment by customer
    engineer = forms.TypedChoiceField(label='')  # choose engineer from db
    engineer.widget.attrs.update({'class': 'app-form-control'})
    # eng_id=forms.CharField(widget=forms.Select(choices=c))
    app_date = forms.DateField(label='', widget=SelectDateWidget(years=range(2022, 2024)))  # date of appointment
    app_date.widget.attrs.update({'class': 'app-form-control-date'})
    app_time = forms.TypedChoiceField(label='')  # time of appointment
    app_time.widget.attrs.update({'class': 'app-form-control'})
    description = forms.CharField(max_length=300, label='',
                                  widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    description.widget.attrs.update({'class': 'app-form-control'})

    def __init__(self, *args, **kwargs):
        super(CustomerAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['engineer'].choices = [(e.id, e.first_name + " " + e.last_name + " (" + e.service_field + ")")
                                           for e in Engineer.objects.filter(status=True).all()]
        # choose engineers from db
        self.fields['app_time'].choices = [('9:00 AM', '9:00 AM'), ('10:00 AM', '10:00 AM'), ('11:00 AM', '11:00 AM'),
                                           ('13:00 PM', '13:00 PM'), ('14:00 PM', '14:00 PM'), ('15:00 PM', '15:00 PM'),
                                           ('16:00 PM', '16:00 PM'), ('17:00 PM', '17:00 PM')]
        # choices for time slot for appointment

    class Meta:
        model = Appointment
        fields = ['description', 'app_date', 'app_time']


# Engineer registration form
class EngineerRegistrationForm(UserCreationForm):  # register engineer
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    username.widget.attrs.update({'class': 'app-form-control'})

    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    email.widget.attrs.update({'class': 'app-form-control'})

    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'}))
    first_name.widget.attrs.update({'class': 'app-form-control'})

    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    last_name.widget.attrs.update({'class': 'app-form-control'})

    dob = forms.DateField(label="", widget=SelectDateWidget(years=range(1960, 2021)))
    dob.widget.attrs.update({'class': 'app-form-control-date'})

    address = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your address'}))
    address.widget.attrs.update({'class': 'app-form-control'})

    city = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'City'}))
    city.widget.attrs.update({'class': 'app-form-control'})

    country = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    country.widget.attrs.update({'class': 'app-form-control'})

    postcode = forms.IntegerField(label="", widget=forms.TextInput(attrs={'placeholder': 'Postcode'}))
    postcode.widget.attrs.update({'class': 'app-form-control'})

    image = forms.ImageField(label="")
    image.widget.attrs.update({'class': 'app-form-control'})

    service_field = forms.CharField(label="", widget=forms.Select(choices=service_field))
    service_field.widget.attrs.update({'class': 'app-form-control'})

    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password1.widget.attrs.update({'class': 'app-form-control'})

    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password again'}))
    password2.widget.attrs.update({'class': 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'service_field', 'dob', 'address', 'city', 'country',
                  'postcode', 'image', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

    def check_date(self):  # form date of birth validator
        cleaned_data = self.cleaned_data
        dob = cleaned_data.get('dob')
        if dob < timezone.now().date():
            return True
        self.add_error('dob', 'Invalid date of birth.')
        return False


# Engineer update details form
class EngineerUpdateForm(forms.ModelForm):  # update engineer details
    first_name = forms.CharField()
    last_name = forms.CharField()
    # age = forms.IntegerField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2022)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)

    # appfees = forms.FloatField()
    # admfees = forms.FloatField()

    class Meta:
        model = Engineer
        fields = ['first_name', 'last_name', 'dob', 'address', 'city', 'country', 'postcode', 'image']
        # 'appfees', 'admfees']


# Engineer approve appointment form
class AppointmentApprovalForm(forms.ModelForm):  # engineer approves an appointment
    description = forms.CharField(max_length=300, label='',
                                  widget=forms.TextInput(attrs={'placeholder': 'DESCRIPTION'}))
    description.widget.attrs.update({'class': 'app-form-control'})
    approval_date = forms.DateField(label='', widget=SelectDateWidget)
    approval_date.widget.attrs.update({'class': 'app-form-control-date'})

    class Meta:
        model = ApprovedCustomerAppointment
        fields = ['description', 'approval_date']


# Engineer edit appointment form
class AppointmentUpdateForm(forms.ModelForm):
    # engineer can edit appointment description field, be it adding new lines or deleting a few of the old one
    description = forms.CharField(max_length=300, label='',
                                  widget=forms.TextInput(attrs={'placeholder': 'DESCRIPTION'}))
    description.widget.attrs.update({'class': 'app-form-control'})

    class Meta:
        model = Appointment
        fields = ['description']


# Feedback form
class FeedbackForm(forms.Form):  # contact us form (feedback), used by customers/engineers to send feedbacks using mail to admins
    APPOINTMENT = 'app'
    BUG = 'b'
    FEEDBACK = 'fb'
    NEW_FEATURE = 'nf'
    OTHER = 'o'
    subject_choices = (
        (APPOINTMENT, 'Appointment'),
        (FEEDBACK, 'Feedback'),
        (NEW_FEATURE, 'Feature Request'),
        (BUG, 'Bug'),
        (OTHER, 'Other'),
    )

    Name = forms.CharField(max_length=30, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    Name.widget.attrs.update({'class': 'form-control'})
    Email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder': 'example@email.com'}))
    Email.widget.attrs.update({'class': 'form-control'})
    Subject = forms.ChoiceField(label='', choices=subject_choices)
    Subject.widget.attrs.update({'class': 'form-control'})
    Message = forms.CharField(max_length=500, label="", widget=forms.TextInput(attrs={'placeholder': 'Enter your message here'}))
    Message.widget.attrs.update({'class': 'form-control'})
