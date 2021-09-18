# Generated by Django 3.2.7 on 2021-09-15 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_auto_20210722_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='messenger',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='messenger',
            name='started',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='GroupMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('messages', models.ManyToManyField(to='messenger.Messenger')),
            ],
        ),
    ]
