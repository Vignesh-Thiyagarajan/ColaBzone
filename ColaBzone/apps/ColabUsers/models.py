from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


# Define a model for different user types
class UserType(models.Model):
    user_type = models.CharField(max_length=50)

    def __str__(self):
        return self.user_type


# Define a custom user manager to handle user creation
class ColabUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True  # Set the user as active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('user_type_id', 1)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# Define the custom user model
class ColabUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=15)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = ColabUserManager()

    # Set the email field as the unique identifier
    USERNAME_FIELD = 'email'

    # Define additional fields that are required for creating a user (empty in this case)
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
