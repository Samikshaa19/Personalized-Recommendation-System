# Generated by Django 3.0.7 on 2021-03-16 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0006_event_user_log_timedetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_user_log',
            name='timedetails',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 12, 16, 40, 498588)),
        ),
    ]
