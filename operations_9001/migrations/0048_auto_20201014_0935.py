# Generated by Django 3.0.2 on 2020-10-14 06:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0048_auto_20201014_0935'),
        ('operations_9001', '0047_auto_20201013_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod9001_providerassessment',
            name='assigned',
            field=models.ForeignKey(default='TEGA483', on_delete=django.db.models.deletion.CASCADE, to='accounts.employees', verbose_name='Assigned to:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mod9001_providerassessment',
            name='due',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Timeline:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='TEGA-M-14102020213', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='TEGA-C-14102020285', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='TEGA-Q-14102020102', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-14102020124', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='emp_perfrev_no',
            field=models.CharField(default='Comp-EA-Q-14102020216', max_length=200, primary_key=True, serialize=False, verbose_name='Performance Review No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='Comp-QP-14102020164', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-14102020270', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-14102020255', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]