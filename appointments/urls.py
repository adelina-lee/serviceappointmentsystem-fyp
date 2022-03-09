from django.contrib.auth import views as auth_views
from django.urls import path

from appointments import views

urlpatterns = [
    path('', views.home_view, name=''),
    path('home/', views.home_view, name='home.html'),

    # Account
    path('login/', views.login_view, name='login.html'),
    path('logout/', auth_views.LogoutView.as_view(template_name='appointments/account/logout.html'), name='logout'),
    # path('wait-approval/', views.wait_approval_view, name='wait_approval.html'), # no need for this
    # Reset password
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='appointments/account/reset_password.html'),
         name='reset_password.html'),
    path('reset_password_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='appointments/account/reset_password_confirm.html'),
         name='password_reset_confirm'),


    # Admin
    path('register/admin/', views.register_adm_view, name='register_adm.html'),  # Admin registration
    path('login/admin/', views.login_adm_view, name='login_adm.html'),  # Admin login
    path('dashboard/admin/', views.dashboard_adm_view, name='dashboard_adm.html'),  # Admin dashboard
    path('profile/admin/', views.profile_adm_view, name='profile_adm.html'),  # Admin profile
    # Admin - Appointments
    path('view/appointments/', views.appointment_adm_view, name='appointment_adm.html'),  # Admin profile
    path('book-appointment-adm/', views.book_app_adm_view, name='book_app_adm.html'),  # Book an appointment
    path('approve-appointment/<int:pk>', views.approve_app_adm_action, name='approve_app_adm_action'),  # Approve an appointment
    path('appointment-admin/complete=<int:pk>', views.complete_app_adm_action, name='complete_app_adm_action'),  # Complete appointment action
    path('appointments/all/', views.all_app_adm_view, name='view_all_app_adm.html'),  # View approved appointments
    path('appointment/details/<int:pk>', views.app_details_adm_view, name='view_app_details_adm.html'),  # View approved appointment's details
    # path('summary-report/', views.summary_report_adm_view, name="summary_report.html"),
    path('download-report/', views.dl_report_adm_action, name="dl_report_adm_action"),
    # Admin - Customers
    path('view/customers/', views.customer_adm_view, name='customer_adm.html'),  # Customers section
    path('approve/customers/', views.approve_cust_adm_view, name='approve_cust.html'),  # Approve customer accounts
    path('approve/customer=<int:pk>', views.approve_cust_adm_action, name='approve_cust_action'), # Approve customer action
    path('view/all-customers/', views.all_cust_adm_view, name='view_all_cust.html'),  # View all customer accounts
    # Admin - Engineers
    path('view/engineers/', views.engineer_adm_view, name='engineer_adm.html'),  # Engineers section
    path('approve/engineers/', views.approve_eng_adm_view, name='approve_eng.html'),  # Approve engineer accounts
    path('approve/engineer=<int:pk>', views.approve_eng_adm_action, name='approve_eng_action'), # Approve engineer action
    path('view/all-engineers/', views.all_eng_adm_view, name='view_all_eng.html'),  # View all engineer accounts
    # Admin - Admin
    path('view/admins/', views.admin_adm_view, name='admin_adm.html'),  # Admins section
    path('approve/admins/', views.approve_adm_adm_view, name='approve_adm.html'),  # Approve engineer accounts
    path('approve/admin=<int:pk>', views.approve_adm_adm_action, name='approve_adm_action'),  # Approve admin action
    path('view/all-admins/', views.all_adm_adm_view, name='view_all_adm.html'),  # View all engineer accounts
    # Statistics
    path('view/statistics/', views.statistics_adm_view, name='view_statistics_adm.html'),  # View appointments statistics
    path('data', views.pivot_data, name='pivot_data'),

    # Customer
    path('register/customer/', views.register_cust_view, name='register_cust.html'),  # Customer registration
    path('login/customer/', views.login_cust_view, name='login_cust.html'),  # Customer login
    path('profile/customer/', views.profile_cust_view, name='profile_cust.html'),  # Customer profile
    path('book-appointment-cust/', views.book_app_cust_view, name='book_app_cust.html'),  # Book an appointment
    path('customer/appointments', views.app_cust_view, name='view_app_cust.html'),  # View pending appointments
    path('customer/appointments/all', views.all_app_cust_view, name='view_all_app_cust.html'),  # View pending appointments
    path('cust-appointment/details/<int:pk>', views.app_details_cust_view, name='view_app_details_cust.html'),  # View appointment details
    path('customer/join-meeting/', views.join_meeting_cust_view, name='join_meeting_cust.html'),  # Join meeting
    path('appointment/report/<int:pk>', views.app_report_cust_view, name='app_report_cust.html'),  # View appointment reports
    path('customer/feedback/', views.feedback_cust_view, name='feedback_cust.html'),

    # Engineer
    path('register/engineer/', views.register_eng_view, name='register_eng.html'),  # Register engineer
    path('login/engineer/', views.login_eng_view, name='login_eng.html'),  # Login engineer
    path('profile/engineer/', views.profile_eng_view, name='profile_eng.html'),  # Engineer profile
    path('dashboard/engineer/', views.dashboard_eng_view, name='dashboard_eng.html'),  # Engineer dashboard
    path('engineer/your-appointments/', views.all_app_eng_view, name='view_app_eng.html'),  # View engineer's appointments
    path('engineer/appointment-details/<int:pk>', views.app_details_eng_view, name='view_app_details_eng.html'),  # Engineer appointment's details
    path('appointment/<int:pk>/<str:link>', views.add_link_eng_action, name='add_link_eng_action'),  # Add link to appointment
    path('engineer/appointment/get=<int:pk>', views.get_link_eng_action, name='get_link_eng_action'),  # Engineer get appointment link action
    path('engineer/appointment/complete=<int:pk>', views.complete_app_eng_action, name='complete_app_eng_action'),  # Complete appointment action
    path('engineer/approved-appointments/', views.approved_app_eng_view, name='view_approved_app_eng.html'),
    path('engineer/approved-appointment-details/<int:pk>', views.approved_app_details_eng_view, name='view_approved_app_details_eng.html'),
    path('engineer/feedback/', views.feedback_eng_view, name='feedback_eng.html'),

    # Report (global)
    path('download/report/id=<int:pk>', views.dl_app_report_action, name="dl_app_report_action"),
    # Download report action
]
