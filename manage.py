#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # 환경 자동 감지
    if "DJANGO_SETTINGS_MODULE" not in os.environ:
        # AWS/운영 환경 감지
        if (
            os.path.exists("/opt/bitnami")  # AWS Lightsail Bitnami
            or os.path.exists("/home/ubuntu")  # AWS EC2 Ubuntu
            or os.environ.get("AWS_EXECUTION_ENV")  # AWS Lambda
            or os.environ.get("SERVER_SOFTWARE", "").startswith("gunicorn")
        ):  # 운영 서버
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")
        else:
            # 로컬 개발 환경
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
