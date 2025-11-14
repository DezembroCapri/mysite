from .base import *
import os
from pathlib import Path

# -------------------------------------------------------------------
# 🧱 BASIC SECURITY SETTINGS
# -------------------------------------------------------------------

DEBUG = False

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "b88c^fo3z8h6s-%=!rr21vwxra!911g@arashw6cuw@2%vlrxj"
)

ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS", "licostech.com,127.0.0.1,localhost"
).split(",")

# -------------------------------------------------------------------
# 📦 STATIC & MEDIA
# -------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"

STORAGES["staticfiles"]["BACKEND"] = (
    "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
)

# -------------------------------------------------------------------
# 🗄️ DATABASE (PostgreSQL RECOMMENDED)
# -------------------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("DB_NAME", "mysite_db"),
        "USER": os.environ.get("DB_USER", "mysite_user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "changeme"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

# -------------------------------------------------------------------
# 📬 EMAIL CONFIG (optional)
# -------------------------------------------------------------------

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST", "")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", "True") == "True"
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")

# -------------------------------------------------------------------
# 🔒 SECURITY HEADERS
# -------------------------------------------------------------------

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# -------------------------------------------------------------------
# 🪵 LOGGING
# -------------------------------------------------------------------

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "django_errors.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": True,
        },
    },
}

# -------------------------------------------------------------------
# 🧩 LOCAL OVERRIDES (optional)
# -------------------------------------------------------------------
try:
    from .local import *
except ImportError:
    pass
