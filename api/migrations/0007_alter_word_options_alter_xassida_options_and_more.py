# Generated by Django 4.1.3 on 2023-07-31 07:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_alter_chapter_options_alter_verse_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="word",
            options={"ordering": ["position"]},
        ),
        migrations.AlterModelOptions(
            name="xassida",
            options={"ordering": ["-modified"]},
        ),
        migrations.AddField(
            model_name="verse",
            name="transcripiton",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
