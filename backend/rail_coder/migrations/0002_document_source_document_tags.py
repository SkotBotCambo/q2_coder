# Generated by Django 4.2.6 on 2023-10-10 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rail_coder", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="source",
            field=models.CharField(default="", max_length=2000),
        ),
        migrations.AddField(
            model_name="document",
            name="tags",
            field=models.CharField(default="", max_length=2000),
        ),
    ]
