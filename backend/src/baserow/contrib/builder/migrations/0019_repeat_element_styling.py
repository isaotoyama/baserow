# Generated by Django 4.1.13 on 2024-05-21 20:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0018_resolve_collection_field_configs"),
    ]

    operations = [
        migrations.AddField(
            model_name="repeatelement",
            name="items_per_row",
            field=models.JSONField(
                default=dict,
                help_text="The amount repetitions per row, per device type. Only applicable when the orientation is horizontal.",
            ),
        ),
        migrations.AddField(
            model_name="repeatelement",
            name="orientation",
            field=models.CharField(
                choices=[("vertical", "Vertical"), ("horizontal", "Horizontal")],
                default="vertical",
                max_length=10,
            ),
        ),
    ]
