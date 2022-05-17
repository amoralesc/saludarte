from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from core.models import Person


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
        verbose_name = _("Site")
        verbose_name_plural = _("Sites")


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        Extra fields may be passed to be stored on the user.
        """
        if not email:
            raise ValueError(_("The given email must be set"))

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


class User(AbstractBaseUser, Person, PermissionsMixin):
    """
    Custom user model. It uses the email as the username (identifier).
    """

    # Abstract user has default fields for:
    # password, last_login

    # Person has default fields for:
    # first_name, last_name, identification_type, identification_number, gender

    email = models.EmailField(
        "email",
        unique=True,
        max_length=255,
        blank=False,
    )

    is_staff = models.BooleanField(
        _("role"),
        default=False,
        help_text=(
            "Designates whether the user can log into " "this admin site."
        ),
    )

    is_active = models.BooleanField(
        _("state"),
        default=True,
        help_text=(
            "Designates whether this user should be "
            "treated as active. Unselect this instead "
            "of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(
        _("date of join"),
        default=timezone.now,
    )

    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        default=1,
        null=True,
        blank=False,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
