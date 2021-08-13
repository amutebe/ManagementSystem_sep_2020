# Generated by Django 3.2.3 on 2021-08-12 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0196_auto_20210812_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='BCL12082021650', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='BCL273', max_length=20, primary_key=True, serialize=False, verbose_name='Employee ID'),
        ),
    ]
