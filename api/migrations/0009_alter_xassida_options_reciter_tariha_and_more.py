# Generated by Django 4.1.3 on 2023-08-15 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0008_rename_transcripiton_verse_transcription"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="xassida",
            options={"ordering": ["slug"]},
        ),
        migrations.AddField(
            model_name="reciter",
            name="tariha",
            field=models.CharField(
                choices=[
                    ("tidjan", "Tidjan"),
                    ("mouride", "Mouride"),
                    ("niassene", "Niassene"),
                    ("layenne", "Layene"),
                    ("khadre", "Khadre"),
                ],
                default="",
                max_length=15,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="audio",
            name="file",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="audio",
            name="xassida",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="audios",
                to="api.xassida",
            ),
        ),
    ]
