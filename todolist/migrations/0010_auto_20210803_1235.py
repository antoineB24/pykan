# Generated by Django 3.2.5 on 2021-08-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0009_timebody_is_todolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='barre',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todolist',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
