# Generated by Django 3.0.6 on 2020-06-02 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Key",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("A", "A"),
                            ("B", "B"),
                            ("C", "C"),
                            ("D", "D"),
                            ("E", "E"),
                            ("F", "F"),
                            ("G", "G"),
                        ],
                        max_length=1,
                    ),
                ),
                ("major", models.BooleanField(default=True)),
            ],
        ),
    ]
