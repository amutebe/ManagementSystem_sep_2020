# Generated by Django 3.0.2 on 2020-08-06 12:18

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('operations_9001', '0016_auto_20200806_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mod9001_incidentregisterstaff',
            name='new_field',
        ),
        migrations.RemoveField(
            model_name='mod9001_incidentregisterstaff',
            name='price',
        ),
        migrations.AddField(
            model_name='mod9001_incidentregisterstaff',
            name='cost',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Financial'), ('2', 'Operational'), ('3', 'Legal/Regulatory'), ('4', 'Brand/Reputation')], default=1, max_length=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='TEGA-M-06082020121', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='TEGA-C-06082020166', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='TEGA-Q-06082020233', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-06082020253', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='Comp-QP-06082020151', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-06082020147', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-06082020111', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]
