from django.db import models
from core.models import Person


class Resident(Person):
    """
    It draws the information of the resident of the organization.
    """

    # Person model includes:
    # first_name, last_name, identification_type, identification_number,

    date_birth = models.DateField(
        "fecha de nacimiento",
        blank=True,
        null=True,
    )

    date_joined = models.DateField(
        "fecha de ingreso",
        blank=True,
        null=True,
    )

    eps = models.CharField(
        "EPS",
        max_length=128,
        blank=True,
    )


SPOUSE = 1
PARENT = 2
SIBLING = 3
CHILD = 4
GRANDPARENT = 5
RELATIVE = 6
FRIEND = 7
OTHER = 8

KINSHIP_CHOICES = (
    (SPOUSE, "Cónyuge"),
    (PARENT, "Padre / Madre"),
    (SIBLING, "Hermano / Hermana"),
    (CHILD, "Hijo / Hija"),
    (GRANDPARENT, "Abuelo / Abuela"),
    (RELATIVE, "Familiar"),
    (FRIEND, "Amigo / Allegado"),
    (OTHER, "Otro"),
)


class Relative(Person):
    """
    It represents a relative of a resident associated via a kinship.
    """

    # Person model includes:
    # first_name, last_name, identification_type, identification_number, gender

    kinship = models.SmallIntegerField(
        "parentesco",
        choices=KINSHIP_CHOICES,
        default=OTHER,
    )

    email = models.EmailField(
        "correo electrónico",
        max_length=255,
        blank=True,
    )

    contact_number = models.CharField(
        "número de contacto",
        max_length=32,
        blank=True,
    )

    email_alerts = models.BooleanField(
        "alertas por correo electrónico",
        default=False,
    )

    whatsapp_alerts = models.BooleanField(
        "alertas por WhatsApp",
        default=False,
    )

    resident = models.ForeignKey(
        Resident,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = "Familiar"
        verbose_name_plural = "Familiares"
