# Generated by Django 3.2.7 on 2021-09-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0007_auto_20210917_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmsg',
            name='subject',
            field=models.CharField(default='', max_length=50),
        ),
    ]
