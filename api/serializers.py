from rest_framework import serializers
from .models import (Audio, Author, AuthorInfo, Chapter, Reciter,
                     TranslatedName, Verse, VerseTranslation, Word, Xassida)


class TranslatedNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatedName
        exclude = ["id", "content_type", "object_id"]


# Reciter and Author Serializers
class ReciterSerializer(serializers.ModelSerializer):
    # translated_name = TranslatedNameSerializer()
    class Meta:
        model = Reciter
        exclude = []


class AuthorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorInfo
        exclude = []


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []
        read_only_fields = ["slug"]


class AuthorWithInfoSerializer(serializers.ModelSerializer):
    info = serializers.SerializerMethodField()

    class Meta:
        model = Author
        exclude = []
        read_only_fields = ["slug"]

    def get_info(self, obj):
        try:
            author_info = obj.infos.get(lang="fr")
        except Exception:
            author_info = None
        return AuthorInfoSerializer(author_info, many=False).data

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        request = self.context["request"]
        ret["picture"] = request.build_absolute_uri(ret["picture"])
        return ret


# Xassida Serializers
class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        exclude = ["id", "verse"]


class VerseTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerseTranslation
        exclude = ["id", "verse"]


class VerseSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    words = WordSerializer(many=True)

    class Meta:
        model = Verse
        fields = ["id", "number", "key", "text", "translations", "transcription", "words"]

    def get_translation_by_lang(self, verse, lang):
        try:
            return verse.translations.get(lang=lang)
        except VerseTranslation.DoesNotExist:
            return None

    def get_translations(self, verse):
        lang = self.context.get('request').query_params.get('lang')
        translation = self.get_translation_by_lang(verse, lang)
        if translation:
            return VerseTranslationSerializer(translation).data
        return None
        

class ChapterSerializer(serializers.ModelSerializer):
    # verses = VerseSerializer(many=True, read_only=True)
    translated_names = TranslatedNameSerializer(many=True, read_only=True)
    verse_count = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = ["id", "name", "number", "translated_names", "verse_count"]

    def get_verse_count(self, obj):
        return len(obj.verses.all())


class XassidaSerializer(serializers.ModelSerializer):
    translated_names = TranslatedNameSerializer(many=True, read_only=True)
    reciters = serializers.SerializerMethodField()
    author = AuthorSerializer()

    class Meta:
        model = Xassida
        fields = [
            "id",
            "author",
            "name",
            "slug",
            "translated_names",
            "chapters",
            "reciters"
        ]
        read_only_fields = ["slug", "reciters"]

    def get_reciters(self, obj):
        audio_reciters = obj.audios.values_list('reciter', flat=True)
        return list(audio_reciters)


# Audio Serializers
class VerseTimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        exclude = []


class AudioSerializer(serializers.ModelSerializer):
    reciter_info = ReciterSerializer(source='reciter', read_only=True)
    xassida_info = XassidaSerializer(source='xassida', read_only=True)

    class Meta:
        model = Audio
        exclude = []

    def validate_file(self, value):
        allowed_extensions = ['.mp3', '.aac', '.m4a']
        if not value.name.lower().endswith(tuple(allowed_extensions)):
            raise serializers.ValidationError("Only .mp3/.aac/.m4a files are allowed.")
        return value
