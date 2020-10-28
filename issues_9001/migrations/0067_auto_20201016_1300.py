# Generated by Django 3.0.2 on 2020-10-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0066_auto_20201016_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='TEGA-IP-Q-16102020879', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-16102020560', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-16102020275', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-16102020209', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-16102020154', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(default='TEGA-IP-Q-16102020685', max_length=200, primary_key=True, serialize=False, verbose_name='ID.:'),
        ),
    ]