# Generated by Django 3.0.2 on 2020-10-14 11:43

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('operations_9001', '0053_auto_20201014_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='TEGA-M-14102020237', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='TEGA-C-14102020198', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='TEGA-Q-14102020157', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-14102020252', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='Initiativenes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Idea Development'), ('2', 'Effective use of resources'), ('3', 'Self drive/motivation')], max_length=5, null=True, verbose_name='Initiativeness & Resourcefulness'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='availabilit',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Time keeping'), ('2', 'Commitment to duty')], max_length=3, null=True, verbose_name='Availability'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='communication',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Oral and Written'), ('2', 'Clarity of Information shared'), ('3', 'Accuracy of Information shared')], max_length=5, null=True, verbose_name='Communication Skills'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='emp_perfrev_no',
            field=models.CharField(default='Comp-EA-Q-14102020232', max_length=200, primary_key=True, serialize=False, verbose_name='Performance Review No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='flexibility',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Relaibility'), ('2', 'Response to Change'), ('3', 'Ease of taking on other roles'), ('4', 'Attitude towards learning')], max_length=7, null=True, verbose_name='Adaptability & Flexibility'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='improveplan',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Job Knowledge'), ('2', 'Adaptability & Flexibility'), ('3', 'Problem Solving'), ('4', 'Initiativeness & Resourcefulness'), ('5', 'Planning & Organisation'), ('6', 'Work quality & quantity'), ('7', 'Interpersonal skills'), ('8', 'Communication skills'), ('9', 'Supervision & Management'), ('10', 'Availability'), ('11', 'Professional contribution')], max_length=23, null=True, verbose_name='Improvement plan'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='interskills',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Relationship with Co-workers'), ('2', 'Clients or Team spirit and general work attitude')], max_length=3, null=True, verbose_name='Interpersonal Skills'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='jobknowledg',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Technical/Professional skills required'), ('2', 'Application'), ('3', 'Support and training to others')], max_length=5, null=True, verbose_name='Job Knowledge'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='nonconformity',
            field=models.CharField(blank=True, choices=[('1', 'Support/Resource'), ('2', 'Planning'), ('3', 'IITS(Information, Instructions, Training, Supervision)'), ('4', 'Performance monitoring'), ('5', 'Evaluation'), ('6', 'Risk/Vulnerability Assessment'), ('7', 'Leadership'), ('8', 'Other')], max_length=200, null=True, verbose_name='Reason: cause of nonconformity'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='planing',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Establishing Priorities'), ('2', 'Meeting Deadlines'), ('3', 'Planning of Tasks')], max_length=5, null=True, verbose_name='Planning & Organisation'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='problemsolving',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Response promptness'), ('2', 'Level of Judgement'), ('3', 'Solution Quality')], max_length=5, null=True, verbose_name='Problem solving'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='professional',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Attendance of Professional Meetings'), ('2', 'Provision of Professional education/talks')], max_length=3, null=True, verbose_name='Professional Contribution'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='supervisionmagt',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Work/task scheduling'), ('2', 'Meeting own/company targets'), ('3', 'Self-Supervision')], max_length=5, null=True, verbose_name='Supervision & Management'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='workquality',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('1', 'Meeting Company Objectives'), ('2', 'Task Completeness'), ('3', 'Accuracy')], max_length=5, null=True, verbose_name='Work Quality & Quantity'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='Comp-QP-14102020169', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-14102020231', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-14102020292', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]