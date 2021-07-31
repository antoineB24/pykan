# Generated by Django 3.2.5 on 2021-07-30 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20210730_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="date de l'action"),
        ),
        migrations.AddField(
            model_name='historique',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="date de l'historique"),
        ),
        migrations.AddField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date de la notif'),
        ),
    ]
