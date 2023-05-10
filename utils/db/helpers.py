import os
import sys
from dataclasses import asdict
from pathlib import Path

import django
from django.core.files import File

sys.path.append("../../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xassida.settings")
django.setup()

from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from api.models import *


def create_author(data, *args):
    """Author insertion"""
    media_path = Path(settings.MEDIA_ROOT)
    media_file = next(media_path.glob("{data['name']}"), None)
    if not media_file:
        img_path = Path(f"../../data/xassidas/{data['tariha']}/{data['name']}")
        img_file = next(img_path.glob("profile.*"), None)
        data["picture"] = File(img_file.open("rb"), data["name"]) if img_file else None
    return Author.objects.update_or_create(name=data["name"], tariha=data["tariha"], defaults=data)[0]


def create_infos(data, author):
    """AuthorInfo insertion
    :param author a Author instance
    """
    obj, _ = AuthorInfo.objects.update_or_create(
        lang=data["lang"], author=author, defaults=data
    )
    return obj


def create_xassidas(data, author):
    """Xassida insertion"""
    author = Author.objects.get(name=author) if (type(author) is str) else author
    del data["translated_lang"]
    obj, _ = Xassida.objects.update_or_create(
        name=data["name"], author=author, defaults=data
    )
    return obj


def create_chapters(data, xassida):
    """Chapter insertion
    :param xassida a Xassida instance
    """
    obj, _ = Chapter.objects.update_or_create(
        number=data["number"], xassida=xassida, defaults=data
    )
    return obj


def create_verses(data, chapter):
    """Verse insertion
    :param chapter a Chapter instance
    """
    obj, _ = Verse.objects.update_or_create(
        number=data["number"], chapter=chapter, defaults=data
    )
    return obj


def create_translations(data, verse):
    """VerseTranslation insertion
    :param verse a Verse instance
    """
    obj, _ = VerseTranslation.objects.update_or_create(
        lang=data["lang"], verse=verse, defaults=data
    )
    return obj


def create_words(data, verse):
    """Word insertion
    :param verse a Verse instance
    """
    obj, _ = Word.objects.update_or_create(
        position=data["position"], verse=verse, defaults=data
    )
    return obj


def create_reciter(data, *args):
    """Reciter insertion"""
    obj, _ = Reciter.objects.update_or_create(name=data["name"], defaults=data)
    return obj


def create_audios(data, xassida):
    """Audio insertion
    :param xassida a xassida instance
    :param reciter a Reciter instance
    """
    reciter = Reciter.objects.get(slug=data["reciter"])
    obj, _ = Audio.objects.update_or_create(
        xassida=xassida, reciter=reciter, defaults=data
    )
    return obj


def create_verse_timings(audio, *args):
    """AudioTiming insertion"""
    obj, _ = VerseTiming.objects.update_or_create(
        audio=audio, verse_number=data["verse_number"], defaults=data
    )
    return obj


def create_translated_names(data, obj):
    """TranslatedName insertion
    :param obj the generic obj
    """
    obj, _ = TranslatedName.objects.update_or_create(
        content_type=ContentType.objects.get_for_model(obj),
        object_id=obj.pk,
        defaults=data,
    )
    return obj
