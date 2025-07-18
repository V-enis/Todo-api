# Generated by Django 5.2.3 on 2025-07-09 20:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_title', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2025, 7, 9, 20, 11, 46, 308225, tzinfo=datetime.timezone.utc))),
                ('status', models.CharField(blank=True, choices=[('n', 'Not started'), ('s', 'Started'), ('c', 'Complete')], default='n', help_text='Task status', max_length=1)),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]
