# Generated by Django 3.0.2 on 2021-03-29 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0104_auto_20210329_1453'),
        ('issues_9001', '0103_auto_20210325_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='TEGA-IP-Q-29032021583', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-29032021522', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='responsibility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='IPresponsibility', to='accounts.employees', verbose_name='Responsibility:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-29032021412', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='responsibility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsibility', to='accounts.employees', verbose_name='Responsibility:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-29032021855', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='responsibility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regulatoryresponsibility', to='accounts.employees', verbose_name='Responsibility:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='responsibility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='riskresponsibility', to='accounts.employees', verbose_name='Responsibility:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-29032021747', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(default='TEGA-IP-Q-2903202162', max_length=200, primary_key=True, serialize=False, verbose_name='ID.:'),
        ),
    ]
