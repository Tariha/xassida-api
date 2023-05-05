#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import *

DEBUG = True

ADMINS = (
       ('Alioune Sall', 'sallalioune99@gmail.com'),
)


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "linzo",
        "PASSWORD": "passer",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
