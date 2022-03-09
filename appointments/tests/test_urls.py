from django.test import SimpleTestCase
from django.urls import reverse, resolve
from appointments.views import *


class TestUrls(SimpleTestCase):

    def test_urls_is_resolved_home(self):  # Home
        url = reverse('')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home_view)

    def test_urls_is_resolved_login(self):  # Login
        url = reverse('login.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_view)

    # Admin
    def test_urls_is_resolved_register_adm(self):  # Register admin
        url = reverse('register_adm.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_adm_view)

    def test_urls_is_resolved_login_adm(self):  # Login admin
        url = reverse('login_adm.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_adm_view)

    def test_urls_is_resolved_dashboard_adm(self):  # Admin dashboard
        url = reverse('dashboard_adm.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, dashboard_adm_view)

    def test_urls_is_resolved_profile_adm(self):  # Admin profile
        url = reverse('profile_adm.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile_adm_view)

    # Admin - Appointments
    def test_urls_is_resolved_appointment_adm(self):  # Admin appointment view
        url = reverse('appointment_adm.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, appointment_adm_view)

    def test_urls_is_resolved_book_app_adm(self):  # Admin appointment booking
        url = reverse('book_app_adm.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, book_app_adm_view)

    def test_urls_is_resolved_view_all_app_adm(self):  # Admin view all appointments
        url = reverse('view_all_app_adm.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_app_adm_view)

    def test_urls_is_resolved_approve_app_adm_action(self):  # Admin approve appointment action
        url = reverse('approve_app_adm_action', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, approve_app_adm_action)

    def test_urls_is_resolved_complete_app_adm_action(self):  # Admin approve appointment action
        url = reverse('complete_app_adm_action', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, complete_app_adm_action)

    def test_urls_is_resolved_app_details_adm(self):  # Admin view appointment details
        url = reverse('view_app_details_adm.html', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, app_details_adm_view)

    # Admin - Customer
    def test_urls_is_resolved_customer_adm_view(self):  # Admin customer view
        url = reverse('customer_adm.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, customer_adm_view)

    def test_urls_is_resolved_approve_cust_adm_view(self):  # Admin approve customer
        url = reverse('approve_cust.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, approve_cust_adm_view)

    def test_urls_is_resolved_view_all_cust_adm(self):  # Admin view all customers
        url = reverse('view_all_cust.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_cust_adm_view)

    # Admin - Engineers
    def test_urls_is_resolved_engineer_adm(self):  # Admin engineer view
        url = reverse('engineer_adm.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, engineer_adm_view)

    def test_urls_is_approve_eng_adm_action(self):  # Admin approve engineer action
        url = reverse('approve_eng_action', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, approve_eng_adm_action)

    def test_urls_is_resolved_approve_eng_adm(self):  # Admin approve engineer view
        url = reverse('approve_eng.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, approve_eng_adm_view)

    def test_urls_is_resolved_view_all_eng_adm(self):  # Admin view all engineers
        url = reverse('view_all_eng.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_eng_adm_view)

    # Admin - Admin
    def test_urls_is_resolved_admin_adm(self):  # Admin views admin
        url = reverse('admin_adm.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, admin_adm_view)

    def test_urls_is_approve_adm_adm_action(self):  # Admin approve admin
        url = reverse('approve_adm_action', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, approve_adm_adm_action)

    def test_urls_is_approve_admin_adm(self):  # Admin approve admin action
        url = reverse('approve_adm.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, approve_adm_adm_view)

    def test_urls_is_view_all_admin_adm(self):  # Admin views all admins
        url = reverse('view_all_adm.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_adm_adm_view)

    # Customer
    def test_urls_is_view_register_cust_view(self):  # Register customer
        url = reverse('register_cust.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_cust_view)

    def test_urls_is_view_login_cust_view(self):  # Login customer
        url = reverse('login_cust.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_cust_view)

    def test_urls_is_view_profile_cust_view(self):  # Profile customer
        url = reverse('profile_cust.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile_cust_view)

    def test_urls_is_view_book_app_cust_view(self):  # Customer book appointment
        url = reverse('book_app_cust.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, book_app_cust_view)

    def test_urls_is_view_app_cust_view(self):  # Customer appointment view
        url = reverse('view_app_cust.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, app_cust_view)

    def test_urls_is_view_all_app_cust_view(self):  # Customer view all appointments
        url = reverse('view_all_app_cust.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_app_cust_view)

    def test_urls_is_view_app_details_cust_view(self):  # Customer view appointment details
        url = reverse('view_app_details_cust.html', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, app_details_cust_view)

    def test_urls_is_view_join_meeting_cust_view(self):  # Customer join a meeting
        url = reverse('join_meeting_cust.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, join_meeting_cust_view)

    def test_urls_is_view_feedback_cust_view(self):  # Customer feedback view
        url = reverse('feedback_cust.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, feedback_cust_view)

    # Engineer
    def test_urls_is_view_register_eng_view(self):  # Register engineer
        url = reverse('register_eng.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, register_eng_view)

    def test_urls_is_view_login_eng_view(self):  # Login engineer
        url = reverse('login_eng.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_eng_view)

    def test_urls_is_view_profile_eng_view(self):  # Engineer profile
        url = reverse('profile_eng.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile_eng_view)

    def test_urls_is_view_dashboard_eng_view(self):  # Engineer dashboard
        url = reverse('dashboard_eng.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, dashboard_eng_view)

    def test_urls_is_view_all_app_eng_view(self):  # Engineer view all appointments
        url = reverse('view_app_eng.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_app_eng_view)

    def test_urls_is_view_app_details_eng_view(self):  # Engineer view appointment details
        url = reverse('view_app_details_eng.html', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, app_details_eng_view)

    def test_urls_is_view_approved_app_eng_view(self):  # Engineer approved appointments view
        url = reverse('view_approved_app_eng.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, approved_app_eng_view)

    def test_urls_is_view_get_link_eng_action(self):  # Engineer complete appointment action
        url = reverse('get_link_eng_action', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, get_link_eng_action)

    def test_urls_is_view_complete_app_eng_action(self):  # Engineer complete appointment action
        url = reverse('complete_app_eng_action', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, complete_app_eng_action)

    def test_urls_is_view_approved_appointment_details_view(self):  # Engineer approved appointments view
        url = reverse('view_approved_app_details_eng.html', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, approved_app_details_eng_view)

    def test_urls_is_view_feedback_eng_view(self):  # Engineer feedback
        url = reverse('feedback_eng.html')
        print(resolve(url))
        self.assertEquals(resolve(url).func, feedback_eng_view)














