# Generated by Django 4.0.4 on 2022-05-18 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Medication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="nombre"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=512,
                        null=True,
                        verbose_name="descripción",
                    ),
                ),
            ],
            options={
                "verbose_name": "Medicamento",
                "verbose_name_plural": "Medicamentos",
            },
        ),
        migrations.CreateModel(
            name="Presentation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.SmallIntegerField(
                        choices=[
                            (1, "Tableta"),
                            (2, "Cápsula"),
                            (3, "Pastilla"),
                            (4, "Gotas"),
                            (5, "Jarabe"),
                            (6, "Inyección"),
                            (7, "Inhalador"),
                        ],
                        verbose_name="tipo",
                    ),
                ),
                (
                    "measure_unit",
                    models.SmallIntegerField(
                        choices=[
                            (1, "mg"),
                            (3, "mg/ml"),
                            (4, "%"),
                            (4, "unidad"),
                        ],
                        verbose_name="unidad de medida",
                    ),
                ),
                ("measure", models.FloatField(verbose_name="medida")),
                (
                    "medication",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="medications.medication",
                        verbose_name="medicamento",
                    ),
                ),
            ],
            options={
                "verbose_name": "Presentación",
                "verbose_name_plural": "Presentaciones",
            },
        ),
    ]