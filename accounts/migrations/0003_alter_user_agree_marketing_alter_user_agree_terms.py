# Generated by Django 5.0 on 2023-12-20 06:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="agree_marketing",
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name="user",
            name="agree_terms",
            field=models.BooleanField(),
        ),
    ]
