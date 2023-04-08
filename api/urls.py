from rest_framework import routers
from .views import *

from django.urls import path, include
from rest_framework_nested import routers
from .views import (
    XassidaViewSet,
    ChapterViewSet,
    VerseViewSet,
    ReciterViewSet,
    AuthorViewSet,
    AudioViewSet,
)

router = routers.SimpleRouter()

# Register Xassida routes
router.register(r'xassidas', XassidaViewSet, basename='xassida')

# Register Reciter routes
router.register(r'reciters', ReciterViewSet, basename='reciter')

# Register Author routes
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = router.urls 
