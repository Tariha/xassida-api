# -*- coding: utf-8 -*-
# Author: Linzo99
# Mail: xxx@xx
# Created Time: Wed Oct 12

from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

# register all ther urls here
router.register(r'authors', AuthorViewSet, 'author')
router.register(r'xassidas', XassidaViewSet, 'xassida')
router.register(r'chapters', ChapterViewSet, 'chapter')
router.register(r'verses', VerseViewSet, 'verse')
router.register(r'audios', AudioViewSet, 'audio')

urlpatterns = router.urls
