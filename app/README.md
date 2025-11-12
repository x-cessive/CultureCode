# The Hitchhiker's Guide to History - Web Application

This is a Flask-based web application for exploring the CultureCode project. It provides an interactive interface to browse, compare, and visualize historical cultures.

## Features

- Browse all documented cultures with rich detail pages
- Compare cultures side-by-side
- Interactive timeline visualization
- API endpoints for programmatic access to cultural data
- Responsive design for desktop and mobile

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/x-cessive/CultureCode.git
   cd CultureCode
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   cd app
   python app.py
   ```

4. Visit `http://localhost:5000` in your browser

## Directory Structure

```
app/
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── index.html         # Home page
│   ├── culture_detail.html # Culture detail page
│   ├── compare.html       # Culture comparison page
│   ├── timeline.html      # Timeline visualization
│   └── error.html         # Error page
├── static/                # Static assets
│   ├── css/               # Stylesheets
│   │   └── style.css      # Main stylesheet
│   └── js/                # JavaScript files
└── (other files...)
```

## API Endpoints

- `GET /api/cultures` - Get all cultures as JSON
- `GET /api/culture/<culture_name>` - Get a specific culture as JSON
- `GET /api/compare/<culture1>/<culture2>` - Compare two cultures

## How It Works

The application reads the culture data from the `cultures/` directory in the main repository, which includes:

- `README.md` - Overview of the culture
- `values.yaml` - Core cultural values
- `social_systems.md` - Social structures
- `innovations.md` - Major innovations
- `timeline.json` - Historical events as "commits"
- `dependencies.json` - Cultural influences

Each culture is treated as a "codebase" of human civilization, with historical events represented as commits, influences as dependencies, and cultural evolution as forks.

## Extending the Application

To extend this application further, you could:

- Add user contribution features
- Integrate with GitHub API for direct repository access
- Add more sophisticated visualization tools
- Implement search and filtering capabilities
- Add historical images and maps
- Create interactive quizzes or learning modules