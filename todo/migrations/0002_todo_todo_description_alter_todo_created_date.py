# Generated by Django 5.2.3 on 2025-07-09 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 7, 9, 20, 21, 29, 224133, tzinfo=datetime.timezone.utc)),
        ),
    ]
