# Generated by Django 3.2 on 2022-05-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_sensoritems_wind_speed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sensoritems',
            options={'verbose_name_plural': 'sensor Items'},
        ),
        migrations.AlterField(
            model_name='sensoritems',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
