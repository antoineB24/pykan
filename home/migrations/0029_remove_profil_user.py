# Generated by Django 3.2.5 on 2021-08-07 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_profil_profil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='user',
        ),
    ]