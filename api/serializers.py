# -*- coding: utf-8 -*-
# Author: Linzo99
# Mail: xxx@xx
# Created Time: Wed Oct 12

from rest_framework import serializers
from .models import *

class TranslatedNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatedName
        exclude = []
        read_only_fields = ['id']

# Reciter and Author Serializers
class ReciterSerializer(serializers.ModelSerializer):
    #translated_name = TranslatedNameSerializer()
    class Meta:
        model = Reciter
        exclude = []
        read_only_fields = ['id']

class AuthorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorInfo
        exclude = []
        read_only_fields = ['id']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []
        read_only_fields = ['id', 'slug']

# Xassida Serializers
class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        exclude = []
        read_only_fields = ['id']

class VerseTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerseTranslation
        exclude = []
        read_only_fields = ['id']

class VerseSerializer(serializers.ModelSerializer):
    translation = VerseTranslationSerializer(read_only=True)
    class Meta:
        model = Verse
        exclude = []
        read_only_fields = ['id']

class ChapterSerializer(serializers.ModelSerializer):
    verses = VerseSerializer(many=True, read_only=True)
    #translated_name = TranslatedNameSerializer()
    class Meta:
        model = Chapter
        exclude = []
        read_only_fields = ['id']

class XassidaSerializer(serializers.ModelSerializer):
    #translated_name = TranslatedNameSerializer()
    chapters = ChapterSerializer(many=True, read_only=True)
    class Meta:
        model = Xassida
        exclude = []
        read_only_fields = ['id', 'slug']
        
# Audio Serializers
class VerseTimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        exclude = []
        read_only_fields = ['id']

class AudioSerializer(serializers.ModelSerializer):
    verse_timings = VerseTimingSerializer(many=True)
    class Meta:
        model = Audio
        exclude = []
        read_only_fields = ['id']
