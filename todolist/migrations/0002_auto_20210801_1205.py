# Generated by Django 3.2.5 on 2021-08-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='action',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todolist',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
