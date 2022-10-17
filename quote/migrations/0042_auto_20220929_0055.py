# Generated by Django 3.1.13 on 2022-09-28 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0041_auto_20220928_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='excise_duty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='idf_fee',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='import_duty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='levies',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='railway_levy',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='vat',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='taxes',
            name='percentage',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='taxes',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100, null=True),
        ),
    ]