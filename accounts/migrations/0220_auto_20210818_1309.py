# Generated by Django 3.2.3 on 2021-08-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0219_auto_20210817_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='BCL18082021273', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='BCL796', max_length=20, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]