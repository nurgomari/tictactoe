# Generated by Django 5.0.7 on 2024-07-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
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
                ("player_x", models.CharField(max_length=50)),
                ("player_o", models.CharField(max_length=50)),
                ("board", models.CharField(default="---------", max_length=9)),
                ("current_turn", models.CharField(default="X", max_length=1)),
                ("winner", models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
    ]
