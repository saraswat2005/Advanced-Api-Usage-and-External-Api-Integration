from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email should be given.')
        user = self.model(
            first_name=first_name,
            email=self.normalize_email(email),
            **extra_fields

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, first_name, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_lawyer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    def __str__(self):
        return self.email


