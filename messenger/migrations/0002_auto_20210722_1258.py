# Generated by Django 3.2.5 on 2021-07-22 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messenger',
            options={'ordering': ['date'], 'verbose_name': 'Messenger'},
        ),
        migrations.AddField(
            model_name='messenger',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date'),
        ),
    ]
