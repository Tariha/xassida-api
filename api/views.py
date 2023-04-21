from rest_framework import status
from rest_framework import filters
import django_filters.rest_framework
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Author, Xassida, Chapter, Verse, Audio, Reciter
from .serializers import AuthorSerializer, XassidaSerializer, ChapterSerializer, VerseSerializer, AudioSerializer, ReciterSerializer

class CustomPagination(PageNumberPagination):
    page_size = 20 

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
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name', 'chapters__verses__words__transcription']
    filterset_fields = ['author', 'author__tariha']
    pagination_class = CustomPagination

class ChapterViewSet(ModelViewSet):
    "Verse Model ViewSet"
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    @action(detail=True, methods=["get"], url_path="verses")
    def getVerses(self, request, *args, **kwargs):
        verses = self.get_object().verses.all()
        paginator = PageNumberPagination()
        paginator.page_size = 20 
        page = paginator.paginate_queryset(verses, request)
        if page is not None:
            serializer = VerseSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = VerseSerializer(verses, many=True)
        return Response(serializer.data)

class AudioViewSet(ModelViewSet):
    "Audio Model ViewSet"
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
