# Generated by Django 3.2 on 2021-09-12 09:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0010_auto_20210803_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionTimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date: ')),
                ('date_started', models.DateTimeField()),
                ('theme', models.CharField(choices=[('blue', 'Blue Theme'), ('red', 'Red Theme'), ('yellow', 'Yellow Theme'), ('green', 'Greene Theme '), ('purple', 'Purple Theme')], default='blue', max_length=50)),
            ],
            options={
                'verbose_name': 'Action Time Table',
                'ordering': ['-date_started'],
            },
        ),
        migrations.DeleteModel(
            name='Time',
        ),
        migrations.DeleteModel(
            name='TimeBody',
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]
