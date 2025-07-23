#!/usr/bin/env python
"""
Post-generation hook for Django ORM cookiecutter template.
This script runs after the project is generated to set up the environment.
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            capture_output=True, 
            text=True
        )
        if result.stdout:
            print(f"   ✅ {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Error: {e.stderr.strip()}")
        return False


def main():
    """Set up the generated project."""
    project_root = Path.cwd()
    print(f"🚀 Setting up Django ORM project at: {project_root}")
    
    # Check if uv is available
    if not run_command("uv --version", "Checking uv installation"):
        print("   ⚠️  uv not found. Please install uv: pip install uv")
        print("   📖 Or visit: https://docs.astral.sh/uv/getting-started/installation/")
        return False
    
    # Create virtual environment
    if not run_command("uv venv", "Creating virtual environment"):
        return False
    
    # Install dependencies
    if not run_command("uv pip install -e .", "Installing project dependencies"):
        return False
    
    # Run Django migrations
    if not run_command("uv run python scripts/manage.py makemigrations", "Creating Django migrations"):
        return False
    
    if not run_command("uv run python scripts/manage.py migrate", "Applying Django migrations"):
        return False
    
    # Create superuser if admin is enabled
    use_admin = "{{ cookiecutter.use_admin }}"
    if use_admin == "yes":
        print("🔑 Django admin is enabled.")
        print("   To create a superuser, run:")
        print(f"   uv run python scripts/manage.py createsuperuser")
        print("   Then start the server with:")
        print(f"   uv run python scripts/manage.py runserver")
        print(f"   Visit: http://127.0.0.1:8000/{{ cookiecutter.admin_url }}/")
    
    # Show usage instructions
    print("\n✨ Project setup complete!")
    print("\n📋 Next steps:")
    print("   1. Activate the environment: source .venv/bin/activate  (Linux/Mac) or .venv\\Scripts\\activate (Windows)")
    print("   2. Run the example script: uv run python src/{{ cookiecutter.package_name }}/main.py")
    print("   3. Add your own models to: src/{{ cookiecutter.package_name }}/models/")
    print("   4. Create migrations: uv run python scripts/manage.py makemigrations")
    print("   5. Apply migrations: uv run python scripts/manage.py migrate")
    
    if use_admin == "yes":
        print("   6. Create admin user: uv run python scripts/manage.py createsuperuser")
        print("   7. Start admin server: uv run python scripts/manage.py runserver")
    
    print("\n🎉 Happy coding with Django ORM!")
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)