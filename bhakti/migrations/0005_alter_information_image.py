# Generated by Django 5.1.5 on 2025-02-01 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bhakti", "0004_alter_information_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="upload/"),
        ),
    ]
