from rest_framework import serializers
from .models import *

class TranslatedNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatedName
        exclude = ['id', 'content_type', 'object_id']

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
        exclude = ['id', 'verse']
        read_only_fields = ['id']

class VerseTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerseTranslation
        exclude = ['id', 'verse']
        read_only_fields = ['id']

class VerseSerializer(serializers.ModelSerializer):
    translations = VerseTranslationSerializer(many=True, read_only=True)
    words = WordSerializer(many=True, read_only=True)
    class Meta:
        model = Verse
        fields = ['id', 'number', 'key', 'text', 'translations', 'words']
        read_only_fields = ['id']

class ChapterSerializer(serializers.ModelSerializer):
    #verses = VerseSerializer(many=True, read_only=True)
    translated_names = TranslatedNameSerializer(many=True, read_only=True)
    class Meta:
        model = Chapter
        fields = ['id', 'name', 'number', 'translated_names']
        read_only_fields = ['id']

class XassidaSerializer(serializers.ModelSerializer):
    translated_names = TranslatedNameSerializer(many=True, read_only=True)
    class Meta:
        model = Xassida
        fields = ['id', 'name', 'slug', 'created', 'modified', 'translated_names']
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
