# Generated by Django 4.2 on 2023-12-27 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Buy",
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
                (
                    "commodity",
                    models.CharField(max_length=100, verbose_name="Commodity"),
                ),
                ("count", models.IntegerField(verbose_name="Count")),
                ("market_value", models.IntegerField(verbose_name="Market_value")),
                (
                    "create_dt",
                    models.DateTimeField(auto_now_add=True, verbose_name="CREATE DT"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
