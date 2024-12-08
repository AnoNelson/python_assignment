#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from kafka_integration.service.email_listener import UserCreatedListener


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospitalmanagement.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    td = UserCreatedListener()
    td.start()
    print("Started Consumer Thread")

if __name__ == '__main__':
    main()

