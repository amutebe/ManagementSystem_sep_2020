# Generated by Django 3.0.2 on 2020-11-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0088_auto_20201106_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='TEGA-IP-Q-06112020867', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-06112020990', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-0611202050', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-06112020511', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-06112020102', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(default='TEGA-IP-Q-0611202072', max_length=200, primary_key=True, serialize=False, verbose_name='ID.:'),
        ),
    ]