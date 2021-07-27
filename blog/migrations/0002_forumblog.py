# Generated by Django 3.2.5 on 2021-07-14 14:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date Sender')),
                ('body', models.TextField(max_length=250)),
            ],
        ),
    ]
