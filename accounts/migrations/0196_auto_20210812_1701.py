# Generated by Django 3.2.3 on 2021-08-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0195_auto_20210812_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='BCL12082021886', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='BCL757', max_length=20, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]