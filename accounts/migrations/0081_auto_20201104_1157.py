# Generated by Django 3.0.2 on 2020-11-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0080_auto_20201104_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA04112020880', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA246', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
