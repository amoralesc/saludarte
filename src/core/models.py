from django.db import models


CC = 1
CE = 2
PA = 3
NUIP = 4

IDENTIFICATION_TYPE_CHOICES = (
    (CC, "C.C."),
    (CE, "C.E."),
    (PA, "Pasaporte"),
    (NUIP, "NUIP"),
)

MALE = 1
FEMALE = 2
UNDEFINED = 3

GENDER_CHOICES = (
    (MALE, "Masculino"),
    (FEMALE, "Femenino"),
    (UNDEFINED, "No definido"),
)


class Person(models.Model):
    """
    Abstract class that represents a person's basic information.
    """

    first_name = models.CharField(
        "nombres",
        max_length=128,
        blank=False,
    )

    last_name = models.CharField(
        "apellidos",
        max_length=128,
        blank=True,
    )

    identification_type = models.SmallIntegerField(
        "tipo de documento",
        choices=IDENTIFICATION_TYPE_CHOICES,
        null=True,
        blank=True,
    )

    identification_number = models.CharField(
        "número de documento",
        max_length=32,
        blank=True,
    )

    gender = models.SmallIntegerField(
        "género", choices=GENDER_CHOICES, default=UNDEFINED, blank=False
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
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
