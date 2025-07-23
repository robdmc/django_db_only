#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django
from pathlib import Path


def setup_django():
    """Set up Django environment."""
    # Add the src directory to Python path
    project_root = Path(__file__).resolve().parent.parent
    src_path = project_root / 'src'
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ cookiecutter.package_name }}.settings')
    django.setup()


def main():
    """Run administrative tasks."""
    setup_django()
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()