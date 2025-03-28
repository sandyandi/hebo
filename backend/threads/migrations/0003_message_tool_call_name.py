# Generated by Django 5.1.4 on 2025-03-06 05:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("threads", "0002_run_organization"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="tool_call_name",
            field=models.CharField(
                blank=True,
                help_text="The name of the tool this message is a response to",
                max_length=255,
                null=True,
            ),
        ),
    ]
