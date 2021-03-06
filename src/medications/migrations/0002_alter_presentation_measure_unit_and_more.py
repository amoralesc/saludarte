# Generated by Django 4.0.4 on 2022-05-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medications", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="presentation",
            name="measure_unit",
            field=models.SmallIntegerField(
                choices=[(1, "mg"), (2, "mg/ml"), (3, "%")],
                verbose_name="unidad de medida",
            ),
        ),
        migrations.AlterField(
            model_name="presentation",
            name="type",
            field=models.SmallIntegerField(
                choices=[
                    (1, "Tabletas"),
                    (2, "Cápsulas"),
                    (3, "Pastillas"),
                    (4, "Gotas"),
                    (5, "Jarabe"),
                    (6, "Inyección"),
                ],
                verbose_name="tipo",
            ),
        ),
    ]
