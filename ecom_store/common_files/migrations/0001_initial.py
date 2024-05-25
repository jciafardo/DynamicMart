# Generated by Django 5.0.6 on 2024-05-14 15:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Products",
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
                ("name", models.CharField(max_length=50)),
                ("quantity", models.IntegerField()),
                ("price", models.FloatField()),
                ("picture", models.ImageField(upload_to="")),
                ("description", models.CharField(max_length=500)),
                ("year", models.IntegerField()),
                ("miles", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="productData",
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
                ("num_sales", models.IntegerField()),
                (
                    "product",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common_files.products",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="cartItems",
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
                ("session", models.CharField(max_length=200)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cart_items",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common_files.products",
                    ),
                ),
            ],
        ),
    ]
