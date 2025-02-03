# Generated by Django 5.1.5 on 2025-02-03 21:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bhakti", "0008_infolist"),
    ]

    operations = [
        migrations.CreateModel(
            name="InfoListInformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveIntegerField()),
                (
                    "info_list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bhakti.infolist",
                    ),
                ),
                (
                    "information",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bhakti.information",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
                "unique_together": {("info_list", "information")},
            },
        ),
    ]
