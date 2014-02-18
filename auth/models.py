'''
accounts.models.py
'''

from django.core.mail import send_mail
from django.contrib.auth.models import (
    User, AbstractBaseUser, BaseUserManager, UserManager)
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Creates and saves a User with the email and password.
    """
    def create_user(self, username, email, password=None): #,**extra_fields):
        user = self.model()
        if not email:
            raise ValueError('Users must have an email address.')
        email = UserManager.normalize_email(email)
        user = self.model(username=username, email=email)
        #user = self.model(username=username, email=email, is_staff=False, is_active=True, is_superuser=False)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password=password)
        user.is_admin = True
        user.save()
        return user

#See: https://docs.djangoproject.com/en/dev/topics/auth/customizing/#specifying-a-custom-user-model
class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=254, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    #USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['email']

    #This must be set to 'email' to require email for login...
    USERNAME_FIELD = 'email'


    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __unicode__(self):
        #return self.email
        return self.username

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

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    #User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
