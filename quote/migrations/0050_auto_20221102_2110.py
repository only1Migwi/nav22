# Generated by Django 3.1.13 on 2022-11-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0049_auto_20221016_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='hs_code_bp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]