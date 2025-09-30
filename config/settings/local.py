from .base import *

# 개발 환경 설정
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# 개발용 데이터베이스 (SQLite)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 개발용 정적 파일 설정
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# 개발용 로깅 (선택사항)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}
