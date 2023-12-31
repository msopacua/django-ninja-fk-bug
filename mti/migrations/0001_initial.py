# Generated by Django 4.2.7 on 2023-11-17 13:24

from django.db import migrations, models
import django.db.models.deletion
import mti.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Developer",
            fields=[
                ("ID", mti.fields.CuidField(max_length=32, serialize=False)),
                ("name", models.CharField(max_length=64)),
                ("company", models.CharField(max_length=32)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("ID", mti.fields.CuidField(max_length=32, serialize=False)),
                ("name", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mti.person",
                    ),
                ),
                ("school", models.CharField(max_length=32)),
            ],
            bases=("mti.person",),
        ),
        migrations.CreateModel(
            name="LinesOfCode",
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
                ("average", models.PositiveSmallIntegerField()),
                (
                    "developer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mti.developer"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReportCard",
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
                ("average", models.PositiveSmallIntegerField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mti.student"
                    ),
                ),
            ],
        ),
    ]
