from rest_framework.viewsets import ModelViewSet
from .models import Author, Xassida, Chapter, Verse, Audio, Reciter
from .serializers import AuthorSerializer, XassidaSerializer, ChapterSerializer, VerseSerializer, AudioSerializer, ReciterSerializer

# Create your views here.
class ReciterViewSet(ModelViewSet):
    "Reciter Model ViewSet"
    queryset = Reciter.objects.all()
    serializer_class = ReciterSerializer

class AuthorViewSet(ModelViewSet):
    "Author Model ViewSet"
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ['tariha']

class XassidaViewSet(ModelViewSet):
    "Author Model ViewSet"
    queryset = Xassida.objects.all()
    serializer_class = XassidaSerializer
    filterset_fields = ['author']

class ChapterViewSet(ModelViewSet):
    "Chapter Model ViewSet"
    #queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_queryset(self):
        xassida_id = self.kwargs['xassida_id']
        return Chapter.objects.filter(xassida__pk=xassida_id)


class VerseViewSet(ModelViewSet):
    "Verse Model ViewSet"
    #queryset = Verse.objects.all()
    serializer_class = VerseSerializer

    def get_queryset(self):
        chapter_id = self.kwargs['chapter_id']
        return Verse.objects.filter(chapter__pk=chapter_id)

class AudioViewSet(ModelViewSet):
    "Audio Model ViewSet"
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
