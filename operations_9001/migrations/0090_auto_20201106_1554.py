# Generated by Django 3.0.2 on 2020-11-06 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations_9001', '0089_auto_20201106_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='TEGA-M-06112020173', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='TEGA-C-06112020229', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_changeregister',
            name='req_no',
            field=models.CharField(default='Comp-RFC-Q-06112020209', max_length=200, primary_key=True, serialize=False, verbose_name='Request No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_correctiveaction',
            name='car_no',
            field=models.CharField(default='Comp-CAR-Q-06112020218', max_length=200, primary_key=True, serialize=False, verbose_name='CAR No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customercomplaint',
            name='comp_no',
            field=models.CharField(default='Comp-COMP-Q-06112020115', max_length=200, primary_key=True, serialize=False, verbose_name='Complaint No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='TEGA-Q-06112020252', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_planning',
            name='car_no',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='operations_9001.mod9001_correctiveaction', verbose_name='CAR ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-06112020128', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='emp_perfrev_no',
            field=models.CharField(default='Comp-EA-Q-06112020103', max_length=200, primary_key=True, serialize=False, verbose_name='Performance Review No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='Comp-QP-06112020242', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-06112020155', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-06112020166', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]