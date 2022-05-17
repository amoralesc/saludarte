from django.db import models

from django.utils.translation import gettext_lazy as _


CC = 1
CE = 2
PA = 3
NUIP = 4

IDENTIFICATION_TYPE_CHOICES = (
    (CC, "C.C."),
    (CE, "C.E."),
    (PA, _("Passport")),
    (NUIP, "NUIP"),
)

MALE = 1
FEMALE = 2
UNDEFINED = 3

GENDER_CHOICES = (
    (MALE, _("Male")),
    (FEMALE, _("Feminino")),
    (UNDEFINED, _("Not defined")),
)


class Person(models.Model):
    """
    Abstract class that represents a person's basic information.
    """

    first_name = models.CharField(
        _("names"),
        max_length=128,
        blank=True,
    )

    last_name = models.CharField(
        _("lastnames"),
        max_length=128,
        blank=True,
    )

    identification_type = models.SmallIntegerField(
        _("identification type"),
        choices=IDENTIFICATION_TYPE_CHOICES,
        default=CC,
        null=True,
        blank=True,
    )

    identification_number = models.CharField(
        _("identification number"),
        max_length=32,
        blank=True,
    )

    gender = models.SmallIntegerField(
        _("gender"),
        choices=GENDER_CHOICES,
        default=UNDEFINED,
    )

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the first name of the user.
        """
        return self.first_name

    def get_formatted_identification(self):
        """
        Returns the identification type and number of the user.
        """
        if self.identification_type is not None:
            return "{} {}".format(
                self.get_identification_type_display(),
                self.identification_number,
            )
        elif self.identification_number is not None:
            return self.identification_number
        else:
            return ""

    class Meta:
        abstract = True
