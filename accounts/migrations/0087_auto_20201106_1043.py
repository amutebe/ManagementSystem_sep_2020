# Generated by Django 3.0.2 on 2020-11-06 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0086_auto_20201106_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA06112020153', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA639', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
