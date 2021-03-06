# Generated by Django 3.0.2 on 2020-10-16 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations_9001', '0063_auto_20201016_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod9001_document_manager',
            name='specifyl',
            field=models.TextField(blank=True, null=True, verbose_name='Specify location:'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='TEGA-M-16102020262', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='TEGA-C-16102020147', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='clause',
            field=models.TextField(blank=True, null=True, verbose_name='Document ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='doc_name',
            field=models.TextField(blank=True, null=True, verbose_name='Document Name:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document',
            field=models.FileField(null=True, upload_to='documents/', verbose_name='Upload document:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_id',
            field=models.TextField(blank=True, null=True, verbose_name='Document ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='TEGA-Q-16102020108', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='retention',
            field=models.CharField(choices=[('1', '1 Year'), ('2', '2 Years'), ('3', '3 years'), ('4', '4 Years'), ('5', '5 years'), ('6', 'more than 5 Yeas')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='version',
            field=models.TextField(blank=True, null=True, verbose_name='Version No:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-16102020159', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='emp_perfrev_no',
            field=models.CharField(default='Comp-EA-Q-16102020169', max_length=200, primary_key=True, serialize=False, verbose_name='Performance Review No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='Comp-QP-16102020265', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-16102020144', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-16102020178', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]
