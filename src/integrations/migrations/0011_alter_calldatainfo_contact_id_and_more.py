# Generated by Django 5.0.1 on 2024-02-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0010_alter_calldatainfo_call_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calldatainfo',
            name='contact_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='calldatainfo',
            name='contact_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='calldatainfo',
            name='contact_parent_lead_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='calldatainfo',
            name='contact_phones',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='calldatainfo',
            name='lead_parent_lead_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
