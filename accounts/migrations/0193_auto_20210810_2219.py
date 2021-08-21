# Generated by Django 3.2.3 on 2021-08-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0192_auto_20210809_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='BCL10082021688', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='BCL911', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]