# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

A Django ORM-only project created with the django_db_only cookiecutter template.

## Features

- 🗄️ **Django ORM**: Full Django ORM functionality without the web framework
- 📦 **Modern Python**: Uses `pyproject.toml` and `uv` package manager
- 🔍 **Auto-discovery**: Automatically imports all models from the models directory
- 📊 **SQLite default**: Ready-to-use SQLite database with PostgreSQL configuration commented out
{% if cookiecutter.use_admin == "yes" -%}
- 🔧 **Django Admin**: Optional web-based admin interface for data management
{%- endif %}
- 🚀 **Example models**: Complete working examples to get you started

## Project Structure

```
{{ cookiecutter.project_name }}/
├── pyproject.toml              # Project dependencies and configuration
├── scripts/
│   └── manage.py              # Django management commands
└── src/
    └── {{ cookiecutter.package_name }}/
        ├── settings.py        # Django configuration
        {% if cookiecutter.use_admin == "yes" -%}
        ├── urls.py           # URL configuration for admin
        {%- endif %}
        ├── main.py           # Example usage script
        └── models/
            ├── __init__.py   # Auto-discovery of models
            ├── example.py    # Example models (Author, Book, Category)
            {% if cookiecutter.use_admin == "yes" -%}
            └── admin.py      # Django admin configuration
            {%- endif %}
```

## Quick Start

1. **Install dependencies**:
   ```bash
   uv venv
   uv pip install -e .
   ```

2. **Set up the database**:
   ```bash
   uv run python scripts/manage.py migrate
   ```

3. **Try the example**:
   ```bash
   uv run python src/{{ cookiecutter.package_name }}/main.py
   ```

{% if cookiecutter.use_admin == "yes" -%}
4. **Create admin user** (optional):
   ```bash
   uv run python scripts/manage.py createsuperuser
   ```

5. **Start admin server** (optional):
   ```bash
   uv run python scripts/manage.py runserver
   ```
   Then visit: http://127.0.0.1:8000/{{ cookiecutter.admin_url }}/
{%- endif %}

## Usage

### Adding Your Own Models

1. Create a new `.py` file in `src/{{ cookiecutter.package_name }}/models/`
2. Define your Django models as usual
3. Models are automatically discovered and imported

Example:
```python
# src/{{ cookiecutter.package_name }}/models/my_models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Using Models in External Scripts

The models package automatically initializes Django when imported, making it easy to use the ORM in external scripts.

**Method 1: Using environment variable**
```bash
export PYTHONPATH="/path/to/{{ cookiecutter.project_name }}/src:$PYTHONPATH"
python your_script.py
```

**Method 2: In your script**
```python
import sys
sys.path.insert(0, '/path/to/{{ cookiecutter.project_name }}/src')

# Import models (Django setup happens automatically)
from {{ cookiecutter.package_name }}.models import *

# ORM is ready to use
MyModel.objects.create(name="Example")
all_objects = MyModel.objects.all()
```

**Method 3: Using pathlib (more robust)**
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "path/to/project/src"))

from {{ cookiecutter.package_name }}.models import *

# Use the ORM
for obj in MyModel.objects.all():
    print(obj.name)
```

**Key Points:**
- Add the `src/` directory (not the project root) to your Python path
- Import from `{{ cookiecutter.package_name }}.models` 
- Django setup happens automatically when you import the models package

### Database Commands

- **Create migrations**: `uv run python scripts/manage.py makemigrations`
- **Apply migrations**: `uv run python scripts/manage.py migrate`
- **Database shell**: `uv run python scripts/manage.py dbshell`
- **Python shell with Django**: `uv run python scripts/manage.py shell`

## Database Configuration

### SQLite (Default)
The project uses SQLite by default with the database file stored as `{{ cookiecutter.database_name }}.sqlite3`.

### PostgreSQL
To use PostgreSQL, uncomment the PostgreSQL configuration in `settings.py` and set environment variables:

```bash
export DB_USER=your_username
export DB_PASSWORD=your_password
```

Then install the PostgreSQL adapter:
```bash
uv add psycopg2-binary
```

## Development Tools

The project includes optional development dependencies:

```bash
uv pip install -e ".[dev]"
```

This adds:
- **black**: Code formatting
- **ruff**: Fast Python linter
- **mypy**: Static type checking
- **django-stubs**: Django type stubs

## Project Information

- **Author**: {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
- **Version**: {{ cookiecutter.version }}
- **Python**: {{ cookiecutter.python_version }}+
- **Django**: 4.2+

{% if cookiecutter.use_admin == "yes" -%}
## Admin Interface

The Django admin interface is enabled and configured with:
- Custom admin classes for all example models
- Search, filtering, and pagination
- Optimized queries with `select_related`
- Inline editing for related objects
- Custom admin site headers

Access the admin at: http://127.0.0.1:8000/{{ cookiecutter.admin_url }}/
{%- endif %}

## License

This project structure was generated from the django_db_only cookiecutter template.