# Generated by Django 3.0.2 on 2020-09-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0031_auto_20200906_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-10092020994', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='description',
            field=models.TextField(blank=True, help_text='Please give comments if any', null=True, verbose_name='Description:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-10092020313', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='interestedparty',
            field=models.CharField(blank=True, choices=[('1', 'Customers'), ('2', 'Regulators'), ('3', 'Hardware/Equipment Suppliers'), ('4', 'Traning providers'), ('5', 'Security providers'), ('6', 'Internet providers'), ('7', 'Insurance providers'), ('8', 'Auditors'), ('9', 'Certification bodies'), ('10', 'Inspectors'), ('11', 'Business partners'), ('12', 'Competitors'), ('13', 'Neighbourhood'), ('14', 'Local authorities'), ('15', 'Family'), ('16', 'Other')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-10092020552', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-1009202066', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
    ]
