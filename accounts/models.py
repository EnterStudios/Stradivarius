'''
accounts.models.py
'''
from django.contrib.auth.models import (
    User, AbstractBaseUser, BaseUserManager, UserManager)
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Creates and saves a User with the email and password.
    """
    def create_user(self, email, password=None):
        user = self.model()
        if not email:
            raise ValueError('Users must have an email address.')
        user = self.model(
            email=CustomUserManager.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    #User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
