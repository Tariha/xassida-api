from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Author, Xassida, Chapter, Verse, Audio, Reciter
from .serializers import AuthorSerializer, XassidaSerializer, ChapterSerializer, VerseSerializer, AudioSerializer, ReciterSerializer

# Create your views here.
class ReciterViewSet(ModelViewSet):
    "Reciter Model ViewSet"
    queryset = Reciter.objects.all()
    serializer_class = ReciterSerializer

    @action(detail=True, methods=['get'], url_path='audios')
    def get_audios(self, request, pk):
        try:
            data = self.get_object().audios
            serializer = AudioSerializer(data, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AuthorViewSet(ModelViewSet):
    "Author Model ViewSet"
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ['tariha']

    @action(detail=True, methods=['get'], url_path='xassidas')
    def get_xassidas(self, request, pk):
        try:
            data = self.get_object().xassidas
            serializer = XassidaSerializer(data, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class XassidaViewSet(ModelViewSet):
    "Author Model ViewSet"
    queryset = Xassida.objects.all()
    serializer_class = XassidaSerializer
    filterset_fields = ['author', 'author__tariha']

    @action(detail=True, methods=['get'], url_path='audios')
    def get_audios(self, request, pk):
        try:
            data = self.get_object().audios
            serializer = AudioSerializer(data, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], url_path='chapters')
    def get_chapters(self, request, pk):
        try:
            data = self.get_object().chapters
            serializer = ChapterSerializer(data, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], url_path='chapters/(?P<number>[0-9]+)')
    def get_chapter_by_number(self, request, pk, number):
        try:
            data = self.get_object().chapters.get(number=number)
            serializer = ChapterSerializer(data)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], url_path='chapters/(?P<number>[0-9]+)/verses')
    def get_verses(self, request, pk, number):
        try:
            data = self.get_object().chapters.get(number=number).verses
            serializer = VerseSerializer(data, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], url_path='chapters/(?P<number>[0-9]+)/verses/(?P<num>[0-9]+)')
    def get_verse_by_number(self, request, pk, number, num):
        try:
            data = self.get_object().chapters.get(number=number).verses.get(number=num)
            serializer = VerseSerializer(data)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ChapterViewSet(ModelViewSet):
    "Chapter Model ViewSet"
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class VerseViewSet(ModelViewSet):
    "Verse Model ViewSet"
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer

class AudioViewSet(ModelViewSet):
    "Audio Model ViewSet"
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
