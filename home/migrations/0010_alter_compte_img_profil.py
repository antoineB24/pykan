# Generated by Django 3.2.5 on 2021-07-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_compte_img_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compte',
            name='img_profil',
            field=models.ImageField(default='profil_photos/default_img.png', upload_to='profil_photos/'),
        ),
    ]
