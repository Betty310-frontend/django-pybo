#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # 환경 변수 DJANGO_ENV로 구분 (없으면 development가 기본)
    django_env = os.environ.get("DJANGO_ENV", "development")

    if "DJANGO_SETTINGS_MODULE" not in os.environ:
        if django_env == "production":
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")
        else:
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
