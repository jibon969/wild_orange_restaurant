from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from .views import (
    register_view,
    logout_view,
    login_view,
    profile_view,
    # AccountEmailActivateView
)

urlpatterns = [
    path('registration/', register_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

    # Change Password !
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/registration/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/registration/password_change_done.html'), name='password_change_done'),

    # Password Reset
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/registration/password_reset.html',
        email_template_name='accounts/registration/password_reset_email.html',
        subject_template_name='accounts/registration/password_reset_subject.txt'), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/registration/password_reset_done.html'), name='password_reset_done'),

    # Reset your password email
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/registration/password_reset_complete.html'), name='password_reset_complete'),

    # For email confirm & activation
    # re_path(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', AccountEmailActivateView.as_view(), name='email-activate'),
    # re_path(r'^email/resend-activation/$', AccountEmailActivateView.as_view(), name='resend-activation'),

]
