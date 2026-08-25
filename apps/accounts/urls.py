
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views


urlpatterns = [
    path('profile/' , views.profile , name='profile'),
    path('login/' , views.login , name='login'),
    path('logout/' , views.logout , name='logout'),
    path('register/' , views.register , name='register'),
    path('change-password/' , views.change_password , name='change_password'),
    path('password-reset/' ,  auth_view.PasswordResetView.as_view(
        template_name = 'accounts/password_reset_form.html',
    ) , name='password_reset'),
    path('password-reset/done/' , auth_view.PasswordResetDoneView.as_view(
        template_name = 'accounts/password_reset_done.html',
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/' , auth_view.PasswordResetConfirmView.as_view(
        template_name = 'accounts/password_reset_confirm.html',
    ), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(
        template_name = 'accounts/password_reset_complete.html',
    ), name='password_reset_complete')
]
