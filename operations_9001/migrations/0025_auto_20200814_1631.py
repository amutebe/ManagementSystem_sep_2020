# Generated by Django 3.0.2 on 2020-08-14 13:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20200814_1631'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations_9001', '0024_auto_20200806_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='adaptability',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID:')),
                ('desc', models.TextField(verbose_name='Description:')),
            ],
        ),
        migrations.CreateModel(
            name='jobknowledg',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ID:')),
                ('desc', models.TextField(verbose_name='Description:')),
            ],
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='TEGA-M-14082020206', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='TEGA-C-14082020293', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='TEGA-Q-14082020291', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-14082020208', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='Comp-QP-14082020153', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-14082020241', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-14082020225', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
        migrations.CreateModel(
            name='mod9001_supplieregistration',
            fields=[
                ('supplier_number', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Supplier no.:')),
                ('date_posted', models.DateField(null=True, verbose_name='Date Posted:')),
                ('name', models.TextField(blank=True, null=True, verbose_name='Supplier Name:')),
                ('manager', models.TextField(blank=True, null=True, verbose_name='Account Manager:')),
                ('contact', models.TextField(blank=True, null=True, verbose_name='Customer Contact Person:')),
                ('phone', models.TextField(blank=True, null=True, verbose_name='Customer Business Phone No:')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Customer Business Email: ')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Customer Business Address: ')),
                ('date_today', models.DateField(default=datetime.datetime.now, verbose_name='Date created:')),
                ('entered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplier_entered_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mod9001_providerassessment',
            fields=[
                ('emp_perfrev_no', models.CharField(default='Comp-EA-Q-14082020183', max_length=200, primary_key=True, serialize=False, verbose_name='Emp.Perf.Review.No.:')),
                ('date', models.DateTimeField(null=True, verbose_name='Date:')),
                ('Provider', models.CharField(choices=[('1', 'External/Supplier'), ('2', 'Internal/Employee')], max_length=200, verbose_name='Provider Type')),
                ('assesment_date', models.DateTimeField(null=True, verbose_name='Last Assessment Date:')),
                ('start', models.DateField(verbose_name='Start Date:')),
                ('end', models.DateField(verbose_name='End Date:')),
                ('purpose', models.TextField(blank=True, null=True, verbose_name='Purpose')),
                ('Communication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='communicatin', to='operations_9001.jobknowledg', verbose_name='8. Communication Skills:')),
                ('adaptability', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adaptabilit', to='operations_9001.jobknowledg', verbose_name='2.\tAdaptability & Flexibility :')),
                ('appraise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appraise', to='accounts.employees', verbose_name='Appraise:')),
                ('availability', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='availabilit', to='operations_9001.jobknowledg', verbose_name='10.\tAvailability')),
                ('initiativeness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='initiative', to='operations_9001.jobknowledg', verbose_name='4.\tInitiativeness & Resourcefulness:')),
                ('jobknowledge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobknowledg', to='operations_9001.jobknowledg', verbose_name='1. Job Knowledge:')),
                ('organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='operations_9001.mod9001_supplieregistration', verbose_name='External Provider Organisation:')),
                ('other', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oter', to='operations_9001.jobknowledg', verbose_name='Other:')),
                ('planner_number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='operations_9001.mod9001_qmsplanner', verbose_name='QMS planner number:')),
                ('planning', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plannin', to='operations_9001.jobknowledg', verbose_name='5. Planning & Organisation:')),
                ('problemsolve', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problemsolve', to='operations_9001.jobknowledg', verbose_name='3.\tProblem Solving:')),
                ('professionalism', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professionalis', to='operations_9001.jobknowledg', verbose_name='11. Professional Contribution:')),
                ('skills', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='operations_9001.jobknowledg', verbose_name='7.\tInterpersonal Skills:')),
                ('supervision', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisio', to='operations_9001.jobknowledg', verbose_name='9. Supervision & Management:')),
                ('work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problemsolv', to='operations_9001.jobknowledg', verbose_name='6.\tWork Quality & Quantity:')),
            ],
        ),
    ]
