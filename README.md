# Django ORM-Only Project Template

This is a cookiecutter template for creating Django projects that use only the ORM functionality without the web framework components.

## Usage

To create a new project using this template:

```bash
cookiecutter django_db_only/
```

## Configuration Questions

When you run cookiecutter, you'll be prompted with the following questions:

### Project Information
- **project_name**: The name of your project (e.g., "My Data Project")
- **package_name**: Auto-generated from project name - the Python package name (lowercase, underscores)
- **project_description**: Brief description of your project (default: "A Django ORM-only project")
- **author_name**: Your full name (default: "Your Name")
- **author_email**: Your email address (default: "your.email@example.com")
- **version**: Initial version number (default: "0.1.0")

### Database Configuration
- **database_name**: Name of the database (auto-generated from package name)
- **database_host**: Database server host (default: "localhost")
- **database_port**: Database server port (default: "5432")

### Optional Features
- **use_admin**: Include Django admin interface? Options: ["no", "yes"] (default: "no")
- **admin_url**: URL path for admin interface (default: "admin") - only used if use_admin is "yes"
- **python_version**: Python version to use (default: "3.11")

## Generated Project Structure

After running cookiecutter, you'll get a project with:

- Basic Django settings configured for ORM-only usage
- Database models structure
- Management scripts
- Example model implementation
- Migration system setup
- Optional Django admin interface (if selected)

## Getting Started

After creating your project:

1. Navigate to your new project directory
2. Install dependencies: `pip install -e .`
3. Configure your database settings in `src/<package_name>/settings.py`
4. Create and run migrations: `python scripts/manage.py makemigrations && python scripts/manage.py migrate`
5. Start building your models in `src/<package_name>/models/`