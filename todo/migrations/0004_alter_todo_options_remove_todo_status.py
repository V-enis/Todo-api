# Generated by Django 5.2.3 on 2025-07-14 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={},
        ),
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
    ]
