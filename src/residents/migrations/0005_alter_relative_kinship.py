# Generated by Django 4.0.4 on 2022-05-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residents', '0004_alter_relative_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relative',
            name='kinship',
            field=models.SmallIntegerField(choices=[(1, 'Cónyuge'), (2, 'Padre / Madre'), (3, 'Hermano / Hermana'), (4, 'Hijo / Hija'), (5, 'Abuelo / Abuela'), (6, 'Familiar'), (7, 'Amigo / Allegado'), (8, 'Otro')], verbose_name='parentesco'),
        ),
    ]