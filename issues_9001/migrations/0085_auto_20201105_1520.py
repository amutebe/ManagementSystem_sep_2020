# Generated by Django 3.0.2 on 2020-11-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0084_auto_20201105_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='TEGA-IP-Q-0511202052', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-05112020176', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-05112020493', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-0511202068', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-05112020370', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(default='TEGA-IP-Q-05112020280', max_length=200, primary_key=True, serialize=False, verbose_name='ID.:'),
        ),
    ]