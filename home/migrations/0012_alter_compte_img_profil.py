# Generated by Django 3.2.5 on 2021-07-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_compte_img_profil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compte',
            name='img_profil',
            field=models.ImageField(default='default_img.png', upload_to=None),
        ),
    ]
