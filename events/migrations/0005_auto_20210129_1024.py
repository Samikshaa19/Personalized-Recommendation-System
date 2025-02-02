# Generated by Django 3.0.7 on 2021-01-29 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210124_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_category_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_category', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='events_model',
            name='e_category',
            field=models.ManyToManyField(to='events.Event_category_model'),
        ),
    ]
