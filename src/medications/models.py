from django.db import models


class Medication(models.Model):
    """
    Represents a medication. A medication may
    be offered in multiple presentations.
    """

    name = models.CharField(
        "nombre",
        max_length=128,
        blank=False,
    )

    description = models.TextField(
        "descripción",
        max_length=512,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"


TABLET = 1
CAPSULE = 2
PILL = 3
DROPS = 4
SYRUP = 5
INJECTION = 6
INHALER = 7


PRESENTATION_TYPE_CHOICES = (
    (TABLET, "Tableta"),
    (CAPSULE, "Cápsula"),
    (PILL, "Pastilla"),
    (DROPS, "Gotas"),
    (SYRUP, "Jarabe"),
    (INJECTION, "Inyección"),
    (INHALER, "Inhalador"),
)


MG = 1
MG_PER_ML = 3
CONCENTRATION = 4
UNIT = 4

PRESENTATION_MEASURE_UNIT_CHOICES = (
    (MG, "mg"),
    (MG_PER_ML, "mg/ml"),
    (CONCENTRATION, "%"),
    (UNIT, "unidad"),
)


class Presentation(models.Model):
    """
    Represents a presentation of a medication.
    """

    medication = models.ForeignKey(
        Medication,
        verbose_name="medicamento",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    type = models.SmallIntegerField(
        "tipo",
        choices=PRESENTATION_TYPE_CHOICES,
        blank=False,
    )

    measure_unit = models.SmallIntegerField(
        "unidad de medida",
        choices=PRESENTATION_MEASURE_UNIT_CHOICES,
        blank=False,
    )

    measure = models.FloatField(
        "medida",
        blank=False,
    )

    class Meta:
        verbose_name = "Presentación"
        verbose_name_plural = "Presentaciones"

    def get_measure_formatted(self):
        return "{0} {1}".format(
            self.measure,
            self.get_measure_unit_display(),
        )
