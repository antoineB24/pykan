# Generated by Django 3.2.7 on 2021-09-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0005_remove_groupmsg_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmsg',
            name='messages',
            field=models.ManyToManyField(to='messenger.Messenger'),
        ),
    ]
