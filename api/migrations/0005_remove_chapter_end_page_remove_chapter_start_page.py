# Generated by Django 4.1.2 on 2022-10-25 15:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_alter_chapter_end_page_alter_chapter_start_page"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="chapter",
            name="end_page",
        ),
        migrations.RemoveField(
            model_name="chapter",
            name="start_page",
        ),
    ]
