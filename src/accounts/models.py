from django.db import models
from django.utils import timezone

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class Site(models.Model):
    """
    The organization has multiple sites. An user can be assigned to one site.
    Implements a default global site, that encompasses all the sites.
    """

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"


CC = 1
CE = 2
PA = 3
NUIP = 4

IDENTIFICATION_TYPE_CHOICES = (
    (CC, "C.C."),
    (CE, "C.E."),
    (PA, "Passport"),
    (NUIP, "NUIP"),
)

MALE = 1
FEMALE = 2
UNDEFINED = 3

GENDER_CHOICES = ((MALE, "Male"), (FEMALE, "Female"), (UNDEFINED, "Undefined"))


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        Extra fields may be passed to be stored on the user.
        """
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Create a default user with the given email and password.
        Extra fields may be passed to be stored on the user.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a superuser with the given email and password.
        Extra fields may be passed to be stored on the user.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model. It uses the email as the username (identifier).
    """

    # Abstract user has default fields for:
    # password, last_login

    # Base account fields:

    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False,
    )

    first_name = models.CharField(
        "first name",
        max_length=30,
        blank=True,
    )

    last_name = models.CharField(
        "last name",
        max_length=150,
        blank=True,
    )

    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text=(
            "Designates whether the user can log into " "this admin site."
        ),
    )

    is_active = models.BooleanField(
        "active",
        default=True,
        help_text=(
            "Designates whether this user should be "
            "treated as active. Unselect this instead "
            "of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(
        "date joined",
        default=timezone.now,
    )

    # Profile information fields:

    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    identification_type = models.PositiveSmallIntegerField(
        choices=IDENTIFICATION_TYPE_CHOICES,
        default=CC,
        null=True,
        blank=True,
    )

    identification_number = models.CharField(
        max_length=20,
        blank=True,
    )

    gender = models.SmallIntegerField(
        choices=GENDER_CHOICES,
        default=UNDEFINED,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the first name for the user."""
        return self.first_name
