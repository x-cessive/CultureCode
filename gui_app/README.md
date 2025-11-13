# The Hitchhiker's Guide to History - Desktop GUI Application

This is a desktop GUI application for the CultureCode project, built with Python and tkinter. It provides the same functionality as the web application but as a standalone desktop application.

## Features

- Browse all documented cultures with rich detail pages
- Compare different civilizations side-by-side
- Timeline visualization of historical events
- Dark/light theme support
- GitHub data refresh capability
- Responsive interface with tabbed views

## Installation

1. Install Python 3.7 or higher
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
   Or for Manjaro/Arch systems:
   ```bash
   sudo pacman -S python-tkinter python-yaml python-markdown python-pillow python-requests
   ```

## Usage

Run the application:
```bash
python main.py
```

The application will load all cultures from the local `cultures/` directory and display them in a searchable list. You can then:

1. Select a culture from the left panel to view its details in the right panel
2. Use the tabs to navigate between different aspects of the culture (Overview, Core Values, Social Systems, etc.)
3. Use the Compare Cultures tool from the Tools menu to compare two civilizations
4. Use the View Timeline tool to see historical events visually
5. Use the File menu to refresh data from GitHub

## Directory Structure

```
gui_app/
├── main.py                 # Main GUI application
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Technical Details

- Built with Python tkinter for native GUI functionality
- Loads data directly from the local CultureCode repository
- Supports both local files and GitHub API fetching
- Responsive layout with paned windows and tabbed interfaces
- Multi-threaded operations to prevent UI blocking

## Extending the Application

To extend this application further, you could:

- Add visualizations using matplotlib or other plotting libraries
- Implement search functionality
- Add image support for historical artifacts
- Create export features (PDF, etc.)
- Add more sophisticated comparison algorithms