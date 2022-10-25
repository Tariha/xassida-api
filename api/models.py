from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify

class EnumTariha(models.TextChoices):
    TIDJIAN = ("tidjian", "Tidjian")
    MOURIDE = ("mouride", "Mouride")
    NIASSENE = ("niassene", "Niassene")
    LAYENE = ("layene", "Layene")
    KHADRE = ("khadre", "Khadre")

# Create your models here.
class TranslatedName(models.Model):
    lang = models.CharField(max_length=2)
    transcription = models.CharField(max_length=100, blank=True, null=True)
    translation = models.CharField(max_length=100, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        indexes = [ models.Index(fields=["content_type", "object_id"])]

class Reciter(models.Model):
    """Reciter Model"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Author(models.Model):
    """Author Model"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    tariha = models.CharField(max_length=15, choices=EnumTariha.choices)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class AuthorInfo(models.Model):
    """AuthorInfo Model"""
    author = models.ForeignKey(Author, models.CASCADE, related_name="infos")
    lang = models.CharField(max_length=2)
    text = models.TextField()

class Xassida(models.Model):
    """Xassida Model"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    author = models.ForeignKey(Author, models.CASCADE, related_name="xassidas")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    """Chapter Model"""
    xassida = models.ForeignKey(Xassida, models.CASCADE, related_name="chapters")
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    start_page = models.IntegerField(blank=True, null=True)
    end_page = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Verse(models.Model):
    """Verse Model"""
    chapter = models.ForeignKey(Chapter, models.CASCADE, related_name="verses")
    number = models.IntegerField()
    key = models.CharField(max_length=10)
    text = models.TextField()

    def __str__(self):
        return self.key


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


class Audio(models.Model):
    """Audio Model"""
    xassida = models.ForeignKey(Xassida, models.CASCADE, related_name="audios")
    reciter = models.ForeignKey(Reciter, models.CASCADE, related_name="audios")
    file = models.FileField()
    duration = models.DurationField(blank=True)

class VerseTiming(models.Model):
    audio = models.ForeignKey(Audio, models.CASCADE, related_name="verse_timings")
    verse_number = models.CharField(max_length=10, blank=True, null=True) 
    timestamp_from =  models.DurationField()
    timestamp_to =  models.DurationField()
    duration =  models.DurationField(blank=True)
