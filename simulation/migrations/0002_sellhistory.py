# Generated by Django 4.2 on 2023-12-27 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("simulation", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SellHistory",
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
                    "sell_time_market_value",
                    models.IntegerField(verbose_name="Sell_time_market_value"),
                ),
                (
                    "create_dt",
                    models.DateTimeField(auto_now_add=True, verbose_name="CREATE DT"),
                ),
                (
                    "buy",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="simulation.buy"
                    ),
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