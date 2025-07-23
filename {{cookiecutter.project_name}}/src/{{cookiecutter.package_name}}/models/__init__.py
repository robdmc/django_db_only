"""
Auto-discovery of Django models.
This module automatically imports all Django model classes from .py files in this directory.
"""

import os
import importlib
import django
from django.conf import settings
from django.db import models

# Initialize Django if not already configured
if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.package_name}}.settings')
    django.setup()

# Get all .py files in the models directory
models_dir = os.path.dirname(__file__)
locals_dict = {}

for filename in os.listdir(models_dir):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = filename[:-3]  # Remove .py extension
        try:
            module = importlib.import_module(f'.{module_name}', package=__name__)
            
            # Find all Django model classes in the module
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (isinstance(attr, type) and 
                    issubclass(attr, models.Model) and 
                    attr is not models.Model and
                    attr.__module__ == module.__name__):  # Only models defined in this module
                    locals_dict[attr_name] = attr
        except ImportError as e:
            # Skip modules that can't be imported
            print(f"Warning: Could not import {module_name}: {e}")
            continue

# Add all discovered models to current namespace
locals().update(locals_dict)

# Create __all__ dynamically for explicit exports
__all__ = list(locals_dict.keys())