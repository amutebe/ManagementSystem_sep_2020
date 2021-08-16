# Generated by Django 3.2.3 on 2021-08-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0216_auto_20210816_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='BCL-IP-Q-16082021215', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='BCL-IP-Q-16082021351', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='BCL-CT-Q-16082021412', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='BCL-IP-LRO-Q-16082021627', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='BCL-RA-16082021890', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(default='BCL-IP-Q-160820217', max_length=200, primary_key=True, serialize=False, verbose_name='ID.:'),
        ),
    ]
