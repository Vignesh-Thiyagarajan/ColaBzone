from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.forms import SetPasswordForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework import permissions
from django.contrib.auth.hashers import make_password  # Import make_password

from ColaBzone.serializers.test import EmptySerializer
from ..serializers.auth import ColabSuperUserSerializer, ColabUserSerializer, ColabUserLoginSerializer


class SuperAdminRegistrationView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ColabSuperUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get the validated data, including the hashed password
        validated_data = serializer.validated_data

        # Hash the user's password using Django's make_password function
        validated_data['password'] = make_password(validated_data['password'])

        # Create the user with the hashed password
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserRegistrationViewSet(SuperAdminRegistrationView):
    serializer_class = ColabUserSerializer


class UserLoginView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ColabUserLoginSerializer  # Replace with your login serializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserLogoutView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmptySerializer  # No serializer needed for logging out

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserForgotPasswordView(PasswordResetView):
    # You can customize the password reset view if needed.
    pass


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordForm  # Use the appropriate form for your project
    post_reset_login = True
