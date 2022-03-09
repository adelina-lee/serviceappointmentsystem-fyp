from django.contrib import admin

from appointments.models import Admin, Customer, Engineer, EngineerServiceField, Appointment, \
    ApprovedCustomerAppointment

admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Engineer)
admin.site.register(EngineerServiceField)
admin.site.register(Appointment)
#  admin.site.register(ApprovedCustomerAppointment)
