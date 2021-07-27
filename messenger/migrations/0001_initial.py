# Generated by Django 3.2.5 on 2021-07-22 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('destinataire', models.CharField(max_length=50)),
                ('sujet', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=1000)),
                ('new', models.BooleanField(default=False)),
            ],
        ),
    ]
