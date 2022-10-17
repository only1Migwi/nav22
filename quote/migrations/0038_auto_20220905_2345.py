# Generated by Django 3.1.13 on 2022-09-05 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0037_auto_20220901_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff_pricing_quotation',
            old_name='buying_terminal_handling2',
            new_name='buying_terminal_handling',
        ),
        migrations.RenameField(
            model_name='staff_pricing_quotation',
            old_name='buying_total_destination',
            new_name='buying_total_A',
        ),
        migrations.RenameField(
            model_name='staff_pricing_quotation',
            old_name='buying_total_origin',
            new_name='buying_total_B',
        ),
        migrations.RenameField(
            model_name='staff_pricing_quotation',
            old_name='margin_total_destination',
            new_name='buying_total_C',
        ),
        migrations.RenameField(
            model_name='staff_pricing_quotation',
            old_name='margin_total_origin',
            new_name='buying_total_D',
        ),
        migrations.RenameField(
            model_name='staff_pricing_quotation',
            old_name='margin_terminal_handling2',
            new_name='margin_terminal_handling',
        ),
        migrations.RenameField(
            model_name='staff_pricing_quotation',
            old_name='selling_total_destination',
            new_name='margin_total_A',
        ),
        migrations.RenameField(
            model_name='staff_pricing_quotation',
            old_name='selling_total_origin',
            new_name='margin_total_B',
        ),
        migrations.RenameField(
            model_name='staff_pricing_quotation',
            old_name='sub_total_duties_bp',
            new_name='margin_total_C',
        ),
        migrations.RenameField(
            model_name='staff_pricing_quotation',
            old_name='sub_total_duties_margin',
            new_name='margin_total_D',
        ),
        migrations.RenameField(
            model_name='staff_pricing_quotation',
            old_name='selling_terminal_handling2',
            new_name='selling_terminal_handling',
        ),
        migrations.RenameField(
            model_name='staff_pricing_quotation',
            old_name='sub_total_duties_sp',
            new_name='selling_total_A',
        ),
        migrations.AddField(
            model_name='staff_pricing_quotation',
            name='selling_total_B',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='staff_pricing_quotation',
            name='selling_total_C',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='staff_pricing_quotation',
            name='selling_total_D',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]