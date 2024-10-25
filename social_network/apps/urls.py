from django.urls import path

# from .views import main_view,register,create_profile_view,otp_view,logout,logout_view,login_view
from django.contrib.auth.views import (PasswordChangeView,PasswordChangeDoneView,PasswordResetDoneView,PasswordResetCompleteView
                                       ,PasswordResetView,PasswordResetConfirmView)
app_name="apps"

urlpatterns = [
    # path('',main_view,name="main_view"),
    # path('register/',register,name="register"),
    # path('otp/',otp_view,name="otp_view"),
    # path('profile/',create_profile_view,name="create_profile_view"),
    # path('login/',login_view,name="login"),
    # path('logout/',logout_view,name="logout"),
    # Password change
    path('password_change/',PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password_change/done/',PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
        # Password reset
    path('password_reset/',PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/done/',PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
