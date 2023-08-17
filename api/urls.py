from django.urls import path
from rest_framework import routers

from .views import (
    XassidaViewSet,
    ReciterViewSet,
    AudioViewSet,
    AuthorViewSet,
    AuthorInfoViewSet,
    ChapterRetrieveView,
    VerseListView,
    PDFView,
)

router = routers.SimpleRouter()

# Register Xassida routes
router.register(r"xassidas", XassidaViewSet, basename="xassida")

# Register Reciter routes
router.register(r"reciters", ReciterViewSet, basename="reciter")

# Register Author routes
router.register(r"authors", AuthorViewSet, basename="author")

# Register AuthorInfo routes
router.register(r"infos", AuthorInfoViewSet, basename="info")

# Register Audio routes
router.register(r"audios", AudioViewSet, basename="audio")

urlpatterns = [
    *router.urls,
    path(r"chapters/<int:pk>/", ChapterRetrieveView.as_view(), name="list-chapters"),
    path(r"chapters/<int:pk>/verses/", VerseListView.as_view(), name="list-verses"),
    path(r"pdf/<pk>", PDFView.as_view(), name="pdf"),
]
