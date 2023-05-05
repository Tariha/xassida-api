#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import *

DEBUG = False

ADMINS = (
       ('Alioune Sall', 'sallalioune99@gmail.com'),
)


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "xassidas",
        "USER": "admin",
        "PASSWORD": "allahiswatching",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
