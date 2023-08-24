from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify


def upload_author(instance, filename):
    return f"images/authors/{instance.slug}/{filename}"


def upload_reciter(instance, filename):
    return f"images/reciters/{instance.slug}/{filename}"


def upload_audio(instance, filename):
    return f"audios/{instance.reciter.slug}/{filename}"


class EnumTariha(models.TextChoices):
    TIDJIAN = ("tidjan", "Tidjan")
    MOURIDE = ("mouride", "Mouride")
    NIASSENE = ("niassene", "Niassene")
    LAYENE = ("layenne", "Layene")
    KHADRE = ("khadre", "Khadre")


# Create your models here.
class TranslatedName(models.Model):
    lang = models.CharField(max_length=2)
    transcription = models.CharField(max_length=100, blank=True, null=True)
    translation = models.CharField(max_length=100, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.transcription

    class Meta:
        indexes = [models.Index(fields=["content_type", "object_id"])]


class Reciter(models.Model):
    """Reciter Model"""

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    picture = models.ImageField(upload_to=upload_reciter, blank=True, null=True)
    tariha = models.CharField(max_length=15, choices=EnumTariha.choices)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def delete(self):
        self.picture.delete()
        return super().delete()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Author(models.Model):
    """Author Model"""

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    picture = models.ImageField(upload_to=upload_author, blank=True, null=True)
    tariha = models.CharField(max_length=15, choices=EnumTariha.choices)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def delete(self):
        self.picture.delete()
        return super().delete()

    def __str__(self):
        name = self.name.replace("-", " ").replace("_", " ")
        return name

    class Meta:
        ordering = ["slug"]


class AuthorInfo(models.Model):
    """AuthorInfo Model"""

    author = models.ForeignKey(Author, models.CASCADE, related_name="infos")
    lang = models.CharField(max_length=2)
    text = models.TextField()


class Xassida(models.Model):
    """Xassida Model"""

    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    author = models.ForeignKey(Author, models.CASCADE, related_name="xassidas")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    translated_names = GenericRelation(TranslatedName)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        name = self.name.replace("-", " ").replace("_", " ")
        return name

    class Meta:
        ordering = ["slug"]


class Chapter(models.Model):
    """Chapter Model"""

    xassida = models.ForeignKey(Xassida, models.CASCADE, related_name="chapters")
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    translated_names = GenericRelation(TranslatedName)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["number"]


class Verse(models.Model):
    """Verse Model"""

    chapter = models.ForeignKey(Chapter, models.CASCADE, related_name="verses")
    number = models.IntegerField()
    key = models.CharField(max_length=10)
    text = models.TextField()
    transcription = models.TextField()

    def __str__(self):
        return self.key

    class Meta:
        ordering = ["number"]


class VerseTranslation(models.Model):
    """VerseTranslation Model"""

    verse = models.ForeignKey(Verse, models.CASCADE, related_name="translations")
    lang = models.CharField(max_length=2)
    text = models.TextField()
    author = models.CharField(max_length=100)


class Word(models.Model):
    """Word Model"""

    verse = models.ForeignKey(Verse, models.CASCADE, related_name="words")
    position = models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=50)
    transcription = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["position"]


class Audio(models.Model):
    """Audio Model"""

    xassida = models.ForeignKey(Xassida, models.DO_NOTHING, related_name="audios")
    reciter = models.ForeignKey(Reciter, models.CASCADE, related_name="audios")
    file = models.FileField(upload_to=upload_audio)
    duration = models.DurationField(blank=True, null=True)

    class Meta:
        ordering = ["reciter__name"]


class VerseTiming(models.Model):
    audio = models.ForeignKey(Audio, models.CASCADE, related_name="verse_timings")
    verse_number = models.CharField(max_length=10, blank=True, null=True)
    timestamp_from = models.DurationField()
    timestamp_to = models.DurationField()
    duration = models.DurationField(blank=True)
