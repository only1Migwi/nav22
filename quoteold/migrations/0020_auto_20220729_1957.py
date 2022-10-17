# Generated by Django 3.1.13 on 2022-07-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0019_quote_air_collection_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote_road',
            name='collection_address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='quote_road',
            name='delivery_address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]