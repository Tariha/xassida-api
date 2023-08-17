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
        read_only_fields = ["id"]


class AuthorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorInfo
        exclude = []
        read_only_fields = ["id"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []
        read_only_fields = ["id", "slug"]


class AuthorWithInfoSerializer(serializers.ModelSerializer):
    info = serializers.SerializerMethodField()

    class Meta:
        model = Author
        exclude = []
        read_only_fields = ["id", "slug"]

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
        read_only_fields = ["id"]


class VerseTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerseTranslation
        exclude = ["id", "verse"]
        read_only_fields = ["id"]


class VerseSerializer(serializers.ModelSerializer):
    translations = serializers.SerializerMethodField()
    words = WordSerializer(many=True)

    class Meta:
        model = Verse
        fields = ["id", "number", "key", "text", "translations", "transcription", "words"]
        read_only_fields = ["id"]

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
        read_only_fields = ["id"]

    def get_verse_count(self, obj):
        return len(obj.verses.all())


class XassidaSerializer(serializers.ModelSerializer):
    translated_names = TranslatedNameSerializer(many=True, read_only=True)
    author = AuthorSerializer()

    class Meta:
        model = Xassida
        fields = [
            "id",
            "author",
            "name",
            "slug",
            "created",
            "modified",
            "translated_names",
            "chapters",
        ]
        read_only_fields = ["id", "slug"]


# Audio Serializers
class VerseTimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        exclude = []
        read_only_fields = ["id"]


class AudioSerializer(serializers.ModelSerializer):
    verse_timings = VerseTimingSerializer(many=True)

    class Meta:
        model = Audio
        exclude = []
        read_only_fields = ["id"]
