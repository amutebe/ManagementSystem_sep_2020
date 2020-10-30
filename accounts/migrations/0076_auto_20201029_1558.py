# Generated by Django 3.0.2 on 2020-10-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0075_auto_20201029_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA29102020407', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA661', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
