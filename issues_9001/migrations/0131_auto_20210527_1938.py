# Generated by Django 3.2.3 on 2021-05-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0130_auto_20210527_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='TEGA-IP-Q-2705202196', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-2705202185', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-27052021204', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-27052021802', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-27052021777', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(default='TEGA-IP-Q-27052021541', max_length=200, primary_key=True, serialize=False, verbose_name='ID.:'),
        ),
    ]
