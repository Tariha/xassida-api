from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"

# For redirection after mail validation
LOGIN_URL = 'http://localhost:3000/login'
