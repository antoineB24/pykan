# Generated by Django 3.2.5 on 2021-08-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_profil_id_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]