# Generated by Django 3.0.7 on 2021-05-28 10:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0019_auto_20210527_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersearch',
            name='time_details',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 10, 55, 21, 374305)),
        ),
    ]
