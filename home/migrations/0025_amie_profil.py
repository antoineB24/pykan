# Generated by Django 3.2.5 on 2021-08-06 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_amie'),
    ]

    operations = [
        migrations.AddField(
            model_name='amie',
            name='profil',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profil', to='home.profil'),
            preserve_default=False,
        ),
    ]