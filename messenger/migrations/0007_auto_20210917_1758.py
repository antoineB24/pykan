# Generated by Django 3.2.7 on 2021-09-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0006_groupmsg_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmsg',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='groupmsg',
            name='destinataire',
            field=models.CharField(default='', max_length=50),
        ),
    ]
