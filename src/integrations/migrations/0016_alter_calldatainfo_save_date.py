# Generated by Django 5.0.1 on 2024-02-09 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0015_alter_calldatainfo_save_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calldatainfo',
            name='save_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 9, 13, 3, 26, 371901, tzinfo=datetime.timezone.utc)),
        ),
    ]
