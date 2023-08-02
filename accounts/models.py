from accounts.utils import unique_key_generator
from wild_orange_restaurant.local_settings import BASE_URL
from datetime import timedelta
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
    AbstractUser
)
from django.db.models import Q
from django.template.loader import get_template
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.conf import settings

DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)


class UserManager(BaseUserManager):
    def create_user(
            self, email, password=None,
            first_name=None,
            last_name=None,
            date_of_birth=None,
            gender=None,
            contact_number=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            contact_number=contact_number
        )
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_staff_user(
            self, email, password,
            first_name, last_name,
            date_of_birth, gender,
            contact_number):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            contact_number=contact_number
        )
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(
            self, email,
            password, first_name,
            last_name, date_of_birth,
            gender, contact_number):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            contact_number=contact_number
        )
        user.is_staff = True
        user.is_admin = True
        # Delete this two line
        user.is_active = True
        # user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email Address', max_length=255, unique=True)
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    date_of_birth = models.DateField(auto_now_add=False)
    contact_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    # notice the absence of a "Password field", that's built in.
    USERNAME_FIELD = 'email'
    # Email & Password are required by default.
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number']

    objects = UserManager()

    def __str__(self):
        return self.email


class EmailActivationQuerySet(models.query.QuerySet):
    def confirmable(self):
        now = timezone.now()
        start_range = now - timedelta(days=DEFAULT_ACTIVATION_DAYS)
        # does my object have a timestamp in here
        end_range = now
        return self.filter(
            activated=False,
            forced_expired=False
        ).filter(
            timestamp__gt=start_range,
            timestamp__lte=end_range
        )


class EmailActivationManager(models.Manager):
    def get_queryset(self):
        return EmailActivationQuerySet(self.model, using=self._db)

    def confirmable(self):
        return self.get_queryset().confirmable()

    def email_exists(self, email):
        return self.get_queryset().filter(
            Q(email=email) |
            Q(user__email=email)
        ).filter(
            activated=False
        )


class EmailActivation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)
    forced_expired = models.BooleanField(default=False)
    expires = models.IntegerField(default=7)  # 7 Days
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = EmailActivationManager()

    def __str__(self):
        return self.email

    def can_activate(self):
        qs = EmailActivation.objects.filter(pk=self.pk).confirmable()  # 1 object
        if qs.exists():
            return True
        return False

    def activate(self):
        if self.can_activate():
            # pre activation user signal
            user = self.user
            user.is_active = True
            user.save()
            # post activation signal for user
            self.activated = True
            self.save()
            return True
        return True

    def regenerate(self):
        self.key = None
        self.save()
        if self.key is not None:
            return True
        return False


""" 
    def send_activation(self):
        if not self.activated and not self.forced_expired:
            if self.key:
                try:
                    base_url = getattr(settings, 'BASE_URL')
                except:
                    base_url = getattr(settings, 'BASE_URL')

                key_path = reverse("email-activate", kwargs={'key': self.key})  # use reverse
                path = "{base}{path}".format(base=base_url, path=key_path)
                context = {
                    'path': path,
                    'email': self.email,
                    'name': self.user.first_name + ' ' + self.user.last_name
                }
                txt_ = get_template("accounts/email/verify.txt").render(context)
                html_ = get_template("accounts/email/verify.html").render(context)
                subject = '1-Click Email Verification'
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [self.email]
                sent_mail = send_mail(
                    subject,
                    txt_,
                    from_email,
                    recipient_list,
                    html_message=html_,
                )
                return sent_mail
        return True
"""


def pre_save_email_activation(sender, instance, *args, **kwargs):
    if not instance.activated and not instance.forced_expired:
        if not instance.key:
            instance.key = unique_key_generator(instance)


pre_save.connect(pre_save_email_activation, sender=EmailActivation)


def post_save_user_create_receiver(sender, instance, created, *args, **kwargs):
    if created:
        obj = EmailActivation.objects.create(user=instance, email=instance.email)
        obj.send_activation()


post_save.connect(post_save_user_create_receiver, sender=User)
