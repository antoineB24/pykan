# Generated by Django 3.2.5 on 2021-08-01 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_auto_20210801_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='time_body',
        ),
        migrations.RemoveField(
            model_name='timebody',
            name='todo_list',
        ),
    ]
