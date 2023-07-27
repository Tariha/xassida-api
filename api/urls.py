from django.urls import path
from rest_framework import routers

from .views import (
    XassidaViewSet,
    ReciterViewSet,
    AuthorViewSet,
    AuthorInfoViewSet,
    ChapterViewSet,
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

# Register Chapter routes
router.register(r"chapters", ChapterViewSet, basename="chapters")

urlpatterns = [
    *router.urls,
    path(r"pdf/<pk>", PDFView.as_view(), name="pdf"),
]
