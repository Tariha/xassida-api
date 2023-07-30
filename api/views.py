import django_filters.rest_framework
from django.views.generic import DetailView
from django_weasyprint import WeasyTemplateResponseMixin
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Audio, Author, AuthorInfo, Chapter, Reciter, Xassida, Verse
from .serializers import (AudioSerializer, AuthorInfoSerializer,
                          AuthorSerializer, AuthorWithInfoSerializer,
                          ChapterSerializer, ReciterSerializer,
                          VerseSerializer, XassidaSerializer)


class CustomPagination(PageNumberPagination):
    page_size = 15


class VersePagination(PageNumberPagination):
    page_size = 20


# Create your views here.
class ReciterViewSet(ReadOnlyModelViewSet):
    "Avoir un ou plusieur recitateurs"
    queryset = Reciter.objects.all()
    serializer_class = ReciterSerializer


class AuthorInfoViewSet(ReadOnlyModelViewSet):
    "Avoir les informations d'un auteur"
    queryset = AuthorInfo.objects.all()
    serializer_class = AuthorInfoSerializer


class AuthorViewSet(ReadOnlyModelViewSet):
    "Avoir un ou plusieur auteurs"
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ["tariha"]

    @action(detail=True, methods=["get"], url_path="info")
    def withInfo(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = AuthorWithInfoSerializer(
            obj, context={"request": request}, many=False
        )
        return Response(serializer.data)


class XassidaViewSet(ReadOnlyModelViewSet):
    "Avoir un ou plusieur xassidas"
    queryset = Xassida.objects.all()
    serializer_class = XassidaSerializer
    filter_backends = [
        filters.SearchFilter,
        django_filters.rest_framework.DjangoFilterBackend,
    ]
    search_fields = ["name", "chapters__verses__words__transcription"]
    filterset_fields = ["author", "author__tariha"]
    pagination_class = CustomPagination


class ChapterRetrieveView(RetrieveAPIView):
    "Avoir une chapitre "
    queryset = Chapter
    serializer_class = ChapterSerializer


class VerseListView(ListAPIView):
    "Avoir les versets d'une chapitre"
    queryset = Verse
    serializer_class = VerseSerializer
    pagination_class = VersePagination

    def get_queryset(self):
        chapter_id = self.kwargs.get("pk")
        queryset = Verse.objects.filter(chapter_id=chapter_id)
        return queryset


class AudioViewSet(ReadOnlyModelViewSet):
    "Audio Model ViewSet"
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer


# --------------------------------------------------------------


class PDFView(WeasyTemplateResponseMixin, DetailView):
    model = Xassida
    context_object_name = "xassida"
    template_name = "pdf_template.html"
    pdf_filename = "foo.pdf"

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        return super().get_context_data(**kwargs)

    def get_pdf_filename(self):
        return f"{self.object.name}.pdf"
