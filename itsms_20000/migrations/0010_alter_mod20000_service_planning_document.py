# Generated by Django 3.2.3 on 2021-08-14 20:39

import accounts.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsms_20000', '0009_alter_mod20000_service_planning_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod20000_service_planning',
            name='document',
            field=models.FileField(null=True, upload_to='documents/', validators=[accounts.utils.validate_file_size], verbose_name='Upload Support Document:'),
        ),
    ]