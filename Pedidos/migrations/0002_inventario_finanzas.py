# Generated by Django 4.1.3 on 2022-12-22 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Pedidos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="inventario",
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
                ("herramientas", models.CharField(max_length=25)),
                ("stock", models.CharField(max_length=3)),
                ("descripcion", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="finanzas",
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
                ("gastos", models.CharField(max_length=10)),
                (
                    "ganancias",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="Pedidos.pedidos",
                    ),
                ),
            ],
        ),
    ]
