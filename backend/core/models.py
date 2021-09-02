from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('Email address is must')

        user = self.model(
            email=self.normalize_email(email), **extra_fields,
            is_active=True,
            is_staff=True,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name


class Task(models.Model):

    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=200)
    user_name = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='user',
        on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    priority = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
