# AccsyBiz - Accessible Business Finder

AccsyBiz is a Django web application that helps users find accessible businesses in Chicago. The application uses business license data from the Chicago Data Portal to provide information about business locations and their accessibility features.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
- [Contributing](#contributing)
- [License](#license)

## About

AccsyBiz addresses the challenge of finding accessible businesses in Chicago. While the city provides business license data through its data portal, there's currently no centralized way to determine which businesses are accessible to people with disabilities. This application allows users to:

- Browse businesses on an interactive map
- View accessibility features for each business
- Contribute accessibility information through user posts
- Upvote/downvote the accuracy of accessibility information

## Features

- **Interactive Map**: Visualize business locations using Leaflet.js
- **Accessibility Information**: View detailed accessibility features for businesses
- **User Contributions**: Registered users can add and update accessibility information
- **Community Validation**: Posts are validated through a voting system (minimum 2 upvotes required)
- **Business Details**: View business information including name, category, and address
- **Search Functionality**: Find businesses by location or name

## Technology Stack

- **Backend**: Python 3.11+, Django 4.2
- **Frontend**: HTML, CSS (Tailwind), JavaScript, Leaflet.js
- **Database**: SQLite (default), easily configurable for PostgreSQL
- **Template Engine**: Django Templates with django-cotton components
- **Rich Text Editor**: django-ckeditor-5
- **Data Processing**: Polars for data analysis
- **Voting System**: django-vote

## Getting Started

### Prerequisites

- Python 3.11+
- pip or uv (package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RexsyBima/django-accsyBiz
   cd django-accsybiz
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install .
   # Or if using uv:
   uv sync
   ```

4. Download the Chicago business license data from the [Chicago Data Portal](https://data.cityofchicago.org/Community-Economic-Development/Business-Licenses-Current-Active-Map/e4sp-itvq) and place it in the project directory, the filename should be `Business_Licenses_-_Current_Active_20250908.csv`.

### Running the Application

1. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

2. Create a superuser (optional):

   ```bash
   python manage.py createsuperuser
   ```

3. Run some django commands:

   ```bash
   python manage.py fillfeatures # To fill initial accessibility features, brailee menu etc
   python manage.py processcsv # To fill the database with business data from the CSV file Business_Licenses_-_Current_Active_20250908.csv
   ```

   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Visit `http://127.0.0.1:8000` in your browser

## Project Structure

```
django-accsybiz/
├── a_core/          # Main Django project settings and configuration
├── a_features/      # Accessibility features management
├── a_pages/         # Static pages (home, about, etc.)
├── a_places/        # Business places and locations
├── a_posts/         # User posts about accessibility features
├── a_users/         # User authentication and profiles
├── templates/       # HTML templates
├── static/          # CSS, JavaScript, and other static assets
├── media/           # User-uploaded files
├── manage.py        # Django CLI utility
├── pyproject.toml   # Project dependencies
└── README.md        # This file
```

## Data Model

The application uses several key models to organize data:

- **Place**: Represents a business with location data (name, address, latitude/longitude)
- **Feature**: Defines accessibility features (wheelchair access, parking, etc.)
- **PlaceFeature**: Junction table linking places to features
- **PostFeature**: User posts about specific place-feature combinations
- **CommentPlace**: Comments on places
- **User**: Django's built-in user model for authentication

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

