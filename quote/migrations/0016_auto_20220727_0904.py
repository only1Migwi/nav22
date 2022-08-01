# Generated by Django 3.1.13 on 2022-07-27 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0015_auto_20220726_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote_air',
            name='quote_serial_no',
        ),
        migrations.RemoveField(
            model_name='quote_road',
            name='quote_serial_no',
        ),
        migrations.RemoveField(
            model_name='quote_sea',
            name='quote_serial_no',
        ),
        migrations.RemoveField(
            model_name='quotetype',
            name='quote_serial_no',
        ),
        migrations.AddField(
            model_name='quote',
            name='quote_serial_no',
            field=models.CharField(default='000', max_length=30),
        ),
    ]