# Generated by Django 5.0.1 on 2024-02-23 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0021_userskpi'),
    ]

    operations = [
        migrations.AddField(
            model_name='userskpi',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
