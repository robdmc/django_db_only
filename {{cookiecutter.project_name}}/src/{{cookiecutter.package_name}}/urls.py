{% if cookiecutter.use_admin == "yes" -%}
"""
URL configuration for {{ cookiecutter.project_name }}
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('{{ cookiecutter.admin_url }}/', admin.site.urls),
]

# Customize admin site headers
admin.site.site_header = "{{ cookiecutter.project_name }} Admin"
admin.site.site_title = "{{ cookiecutter.project_name }}"
admin.site.index_title = "Welcome to {{ cookiecutter.project_name }} Administration"
{%- endif %}