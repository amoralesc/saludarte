# Generated by Django 4.0.4 on 2022-05-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_user_email_alter_user_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="identification_type",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[
                    (1, "C.C."),
                    (2, "C.E."),
                    (3, "Pasaporte"),
                    (4, "NUIP"),
                ],
                default=1,
                null=True,
                verbose_name="identification type",
            ),
        ),
    ]
