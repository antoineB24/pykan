# Generated by Django 3.2.5 on 2021-08-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20210801_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]