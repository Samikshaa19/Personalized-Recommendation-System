# Generated by Django 3.0.7 on 2021-05-26 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0011_auto_20210328_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyrecommendedevents',
            name='latest_update',
            field=models.DateField(default=datetime.date(2021, 5, 26)),
        ),
    ]
