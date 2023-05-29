# Generated by Django 4.1.5 on 2023-05-29 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_rename_task_tasks"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=200)),
                ("completed", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(name="Tasks",),
    ]