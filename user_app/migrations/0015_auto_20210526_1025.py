# Generated by Django 3.0.7 on 2021-05-26 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0014_auto_20210526_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersearch',
            name='time_details',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 26, 10, 25, 35, 452168)),
        ),
    ]
