# Generated by Django 3.0.7 on 2021-01-24 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210124_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events_model',
            name='e_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
