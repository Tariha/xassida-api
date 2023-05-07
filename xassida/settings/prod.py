#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import *
from django.core.management.utils import get_random_secret_key


DEBUG = False

SECRET_KEY = get_random_secret_key() 

SECURE_HSTS_SECONDS = 2_592_000  # 30 days
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

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
