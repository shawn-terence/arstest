# Generated by Django 4.2.13 on 2024-06-22 07:39

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_user_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="image",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, verbose_name="image"
            ),
        ),
    ]
