# Generated by Django 4.0 on 2022-02-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0014_rename_transpired_at_workshop_scheduled_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workshop",
            name="scheduled_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]