# Generated by Django 3.1.13 on 2022-07-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0018_auto_20220727_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote_air',
            name='collection_address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]