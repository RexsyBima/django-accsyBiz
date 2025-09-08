# Project Context for Qwen Code

## Project Overview

This is a Django web application project named `django-accsybiz`. It's a Python-based web framework project using Django 5.2.6. The project appears to be in its early stages, with a basic setup including core Django configuration files, a templates directory, and a simple base HTML template.


## Goal

The goal of this project is to facilitate a accessbility information in the business that is happening in Chicago. by using the the business license data from chicago data portal, we can get the information about the businesses that are in Chicago. The issue is as far as we know, there is no way to know if such business is accessible or not. This project will help us to get the information about accessibility of the business.

## Key Technologies

- Python 3.11+
- Django 5.2.6
- SQLite (default database)

## Project Structure

- `a_core/`: Contains the main Django project settings, URL configurations, and WSGI/ASGI files.
- `templates/`: Contains HTML templates, starting with a `base.html`.
- `manage.py`: Django's command-line utility for administrative tasks.
- `pyproject.toml`: Project metadata and dependencies (using `django` and `django-stubs`).

## Building and Running

1.  **Setup**: Ensure Python 3.11+ is installed. Create and activate a virtual environment.
2.  **Install Dependencies**: Use `pip install .` or `pip install -e .` (for editable install) based on `pyproject.toml`. Alternatively, if using a tool like `uv`, use `uv sync`.
3.  **Run Migrations**: Execute `python manage.py migrate` to set up the database.
4.  **Start Development Server**: Run `python manage.py runserver` to start the development server, typically accessible at `http://127.0.0.1:8000`.

## Development Conventions

- Django's default project structure is used.
- Templates are stored in the `templates/` directory.
- Static files (CSS, JS) are expected to be in a `static/` directory (referenced in `base.html`).
- Settings are configured for development (`DEBUG = True`).

## Key Files

- `a_core/settings.py`: Main Django settings file.
- `a_core/urls.py`: Main URL configuration.
- `templates/base.html`: Base HTML template.
- `manage.py`: Entry point for Django CLI commands.
- `pyproject.toml`: Project dependencies and metadata.
