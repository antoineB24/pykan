# Generated by Django 3.2.7 on 2021-09-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiJson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apijson',
            name='body',
            field=models.JSONField(default={}),
        ),
    ]
