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

class XassidaViewSet(ModelViewSet):
    "Author Model ViewSet"
    queryset = Xassida.objects.all()
    serializer_class = XassidaSerializer

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
