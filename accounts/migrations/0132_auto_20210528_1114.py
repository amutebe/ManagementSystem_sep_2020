# Generated by Django 3.2.3 on 2021-05-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0131_auto_20210527_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA28052021859', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA861', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
