# Generated by Django 3.0.7 on 2021-05-26 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0018_auto_20210526_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_user_log',
            name='timedetails',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 26, 9, 26, 19, 564814)),
        ),
    ]
