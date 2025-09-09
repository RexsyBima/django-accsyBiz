# Project Context for Qwen Code

## Project Overview

This is a Django web application project named `django-accsybiz`. It's a Python-based web framework project using Django 5.2.6. The project is designed to provide accessibility information for businesses in Chicago by using business license data from the Chicago Data Portal.

## Goal

The goal of this project is to facilitate accessibility information for businesses in Chicago. By using business license data from the Chicago Data Portal, we can get information about businesses in Chicago. The issue is that there is currently no way to know if such businesses are accessible or not. This project will help provide information about the accessibility of businesses.

## Key Technologies

- Python 3.11+
- Django 5.2.6
- SQLite (default database)
- django-ckeditor-5 for rich text editing
- django-cotton for component-based templates
- polars for data processing
- Leaflet.js for mapping

## Project Structure

- `a_core/`: Contains the main Django project settings, URL configurations, and WSGI/ASGI files.
- `a_features/`: Django app for managing accessibility features that can be associated with places.
- `a_pages/`: Django app for main pages like home, about, etc.
- `a_places/`: Django app for managing business places and their locations.
- `a_posts/`: Django app for user-generated content related to places and features.
- `templates/`: Contains HTML templates organized by app.
- `media/`: Directory for user-uploaded media files.
- `manage.py`: Django's command-line utility for administrative tasks.
- `pyproject.toml`: Project metadata and dependencies.
- `uv.lock`: Lock file for uv package manager.

## Application Architecture

The project is organized into several Django apps:

1. **a_places**: Manages business place information including name, address, location (latitude/longitude), and business category.
2. **a_features**: Defines accessibility features that can be associated with places.
3. **a_posts**: Handles user-generated content about places and their accessibility features, including voting functionality.
4. **a_pages**: Manages static pages like home, about, etc.

## Data Model

- **Place** (a_places): Represents a business with location data, business details, and license information.
- **Feature** (a_features): Defines accessibility features (e.g., wheelchair access, parking, etc.).
- **PlaceFeature** (a_places): Junction table linking places to features.
- **PostFeature** (a_posts): User posts about specific place-feature combinations with rich text content.
- **PostFeatureVote** (a_posts): Voting system for user posts.
- **CommentPlace** (a_posts): Comments on places.

## Building and Running

1.  **Setup**: Ensure Python 3.11+ is installed. Create and activate a virtual environment.
2.  **Install Dependencies**: Use `pip install .` or `pip install -e .` (for editable install) based on `pyproject.toml`. Alternatively, if using a tool like `uv`, use `uv sync`.
3.  **Run Migrations**: Execute `python manage.py migrate` to set up the database.
4.  **Start Development Server**: Run `python manage.py runserver` to start the development server, typically accessible at `http://127.0.0.1:8000`.

## Development Conventions

- Django's default project structure is used with multiple apps for different functionality.
- Templates are stored in the `templates/` directory, organized by app.
- Static files (CSS, JS) are expected to be in a `static/` directory.
- Settings are configured for development (`DEBUG = True`).
- Uses django-cotton for component-based templating.
- Uses django-ckeditor-5 for rich text editing in posts.
- Media files are stored in the `media/` directory.

## Key Files

- `a_core/settings.py`: Main Django settings file with configurations for all apps, database, static files, and CKEditor.
- `a_core/urls.py`: Main URL configuration routing to different apps.
- `templates/base.html`: Base HTML template with Leaflet.js for mapping.
- `manage.py`: Entry point for Django CLI commands.
- `pyproject.toml`: Project dependencies and metadata.
- `a_places/models.py`: Defines Place and PlaceFeature models.
- `a_features/models.py`: Defines Feature model.
- `a_posts/models.py`: Defines PostFeature, PostFeatureVote, and CommentPlace models.