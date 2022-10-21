import sys, os, django
from dataclasses import asdict

sys.path.append('../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xassida.settings")
django.setup()

from api.models import *

def create_author(data, *args):
    """Author insertion
    """
    obj,_ = Author.objects.update_or_create(name=data['name'], tariha=data['tariha'], defaults=data) 
    return obj

def create_infos(data, author):
    """AuthorInfo insertion
       :param author a Author instance
    """
    obj,_ = AuthorInfo.objects.update_or_create(lang=data['lang'], author=author, defaults=data) 
    return obj

def create_xassidas(data, author):
    """Xassida insertion"""
    obj,_ = Xassida.objects.update_or_create(name=data['name'], author=author, defaults=data) 
    return obj

def create_chapters(data, xassida):
    """Chapter insertion
       :param xassida a Cassida instance
    """
    obj,_ = Chapter.objects.update_or_create(name=data['name'], xassida=xassida, defaults=data) 
    return obj

def create_verses(data, chapter):
    """Verse insertion
       :param chapter a Chapter instance
    """
    obj,_ = Verse.objects.update_or_create(number=data['number'], chapter=chapter, defaults=data) 
    return obj

def create_translations(data, verse):
    """VerseTranslation insertion
       :param verse a Verse instance
    """
    obj,_ = VerseTranslation.objects.update_or_create(lang=data['lang'], verse=verse, defaults=data) 
    return obj

def create_words(data, verse):
    """Word insertion
       :param verse a Verse instance
    """
    obj,_ = Word.objects.update_or_create(position=data['position'], verse=verse, defaults=data) 
    return obj

def create_reciter(data, *args):
    """Reciter insertion
    """
    obj,_ = Reciter.objects.update_or_create(name=data['name'], defaults=data) 
    return obj

def create_audios(data, xassida):
    """Audio insertion
       :param xassida a xassida instance
       :param reciter a Reciter instance
    """
    reciter = Reciter.objects.get(slug=data['reciter']) 
    obj,_ = Audio.objects.update_or_create(xassida=xassida, reciter=reciter, defaults=data) 
    return obj

def create_verse_timings(audio, *args):
    """AudioTiming insertion
    """
    obj,_ = VerseTiming.objects.update_or_create(audio=audio, verse_number=data['verse_number'], defaults=data) 
    return obj

def create_translated_names(data, obj):
    """TranslatedName insertion
       :param obj the generic obj
    """
    obj,_ = Audio.objects.update_or_create(content_type=obj, object_id=obj.pk, defaults=data) 
    return obj
