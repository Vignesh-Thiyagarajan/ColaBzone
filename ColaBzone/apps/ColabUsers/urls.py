from django.urls import path
from django.contrib.auth.views import PasswordResetConfirmView
from .views.auth import SuperAdminRegistrationView, UserRegistrationViewSet, UserLoginView, UserLogoutView, \
    UserForgotPasswordView

urlpatterns = [
    path('register/admin/', SuperAdminRegistrationView.as_view(), name='user-registration'),
    path('register/user/', UserRegistrationViewSet.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('forgot-password/', UserForgotPasswordView.as_view(), name='forgot-password'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
