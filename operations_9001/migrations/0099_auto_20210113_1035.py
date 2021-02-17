# Generated by Django 3.0.2 on 2021-01-13 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operations_9001', '0098_auto_20210102_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod9001_customersatisfaction',
            name='rankdesc',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Final Rating: (Rank Description'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='TEGA-M-13012021260', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='TEGA-C-13012021168', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_changeregister',
            name='req_no',
            field=models.CharField(default='Comp-RFC-Q-13012021238', max_length=200, primary_key=True, serialize=False, verbose_name='Request No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_correctiveaction',
            name='car_no',
            field=models.CharField(default='Comp-CAR-Q-13012021231', max_length=200, primary_key=True, serialize=False, verbose_name='CAR No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customercomplaint',
            name='comp_no',
            field=models.CharField(default='Comp-COMP-Q-13012021152', max_length=200, primary_key=True, serialize=False, verbose_name='Complaint No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_customersatisfaction',
            name='satis_no',
            field=models.CharField(default='Comp-CS-Q-13012021247', max_length=200, primary_key=True, serialize=False, verbose_name='Satisfaction Survey No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='TEGA-Q-13012021174', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='standard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard', to='operations_9001.document_standard', verbose_name='Standard'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-13012021207', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='emp_perfrev_no',
            field=models.CharField(default='Comp-EA-Q-13012021154', max_length=200, primary_key=True, serialize=False, verbose_name='Performance Review No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='Comp-QP-13012021169', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-13012021188', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-13012021182', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]