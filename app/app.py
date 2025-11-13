#!/usr/bin/env python3
"""
The Hitchhiker's Guide to History - A CultureCode Web Application
A Flask-based application to explore the CultureCode repository
"""

import json
import yaml
import os
from pathlib import Path
from flask import Flask, render_template, request, jsonify
import markdown
from datetime import datetime

from github_fetcher import fetch_culture_data, fetch_all_cultures as fetch_all_from_github


app = Flask(__name__)

# Configuration - Use local files as fallback, but can fetch from GitHub
USE_GITHUB_FETCH = os.getenv('USE_GITHUB_FETCH', 'false').lower() == 'true'
CULTURES_DIR = Path(__file__).parent.parent / "cultures"
SCHEMA_DIR = Path(__file__).parent.parent / "schema"


def load_culture_data(culture_name):
    """
    Load culture data either from local files or from GitHub.
    This function maintains backward compatibility with the local file approach
    while providing the option to fetch from GitHub.
    """
    if USE_GITHUB_FETCH:
        # Fetch from GitHub
        data = fetch_culture_data(culture_name)
    else:
        # Use local files (original implementation)
        culture_path = CULTURES_DIR / culture_name
        
        if not culture_path.exists():
            # If local files don't exist, try fetching from GitHub
            data = fetch_culture_data(culture_name)
        else:
            data = {"name": culture_name, "directory": culture_name}
            
            # Load README
            readme_path = culture_path / "README.md"
            if readme_path.exists():
                with open(readme_path, 'r', encoding='utf-8') as f:
                    data['readme_raw'] = f.read()
                    data['readme_html'] = markdown.markdown(f.read())
            
            # Load values
            values_path = culture_path / "values.yaml"
            if values_path.exists():
                with open(values_path, 'r', encoding='utf-8') as f:
                    try:
                        data['values'] = yaml.safe_load(f)
                    except yaml.YAMLError:
                        data['values'] = {}
            
            # Load social systems
            social_path = culture_path / "social_systems.md"
            if social_path.exists():
                with open(social_path, 'r', encoding='utf-8') as f:
                    data['social_systems_raw'] = f.read()
                    data['social_systems_html'] = markdown.markdown(f.read())
            
            # Load innovations
            innovations_path = culture_path / "innovations.md"
            if innovations_path.exists():
                with open(innovations_path, 'r', encoding='utf-8') as f:
                    data['innovations_raw'] = f.read()
                    data['innovations_html'] = markdown.markdown(f.read())
            
            # Load timeline
            timeline_path = culture_path / "timeline.json"
            if timeline_path.exists():
                with open(timeline_path, 'r', encoding='utf-8') as f:
                    try:
                        data['timeline'] = json.load(f)
                    except json.JSONDecodeError:
                        data['timeline'] = []
            
            # Load dependencies
            dependencies_path = culture_path / "dependencies.json"
            if dependencies_path.exists():
                with open(dependencies_path, 'r', encoding='utf-8') as f:
                    try:
                        data['dependencies'] = json.load(f)
                    except json.JSONDecodeError:
                        data['dependencies'] = {}
    
    # Extract key information from README for easy template access
    if 'readme_raw' in data:
        readme = data['readme_raw']
        
        # Extract time period
        time_period = "Time period not specified"
        for line in readme.split('\n'):
            if 'Time Period:' in line:
                time_period = line.replace('**Time Period:**', '').replace('**', '').strip()
                break
        data['time_period'] = time_period
        
        # Extract geography
        geography = "Geography not specified"
        for line in readme.split('\n'):
            if 'Geography:' in line:
                geography = line.replace('**Geography:**', '').replace('**', '').strip()
                break
        data['geography'] = geography
        
        # Extract political system
        political_system = "Political system not specified"
        for line in readme.split('\n'):
            if 'Political System:' in line:
                political_system = line.replace('**Political System:**', '').replace('**', '').strip()
                break
        data['political_system'] = political_system
        
        # Extract major innovations
        major_innovations = "Major innovations not specified"
        for line in readme.split('\n'):
            if 'Major Innovations:' in line:
                major_innovations = line.replace('**Major Innovations:**', '').replace('**', '').strip()
                break
        data['major_innovations'] = major_innovations
    else:
        # Set defaults if readme is not available
        data['time_period'] = "Time period not specified"
        data['geography'] = "Geography not specified"
        data['political_system'] = "Political system not specified"
        data['major_innovations'] = "Major innovations not specified"
    
    return data


def get_all_cultures():
    """
    Get a list of all available cultures.
    Uses GitHub fetcher if configured, otherwise uses local files.
    """
    if USE_GITHUB_FETCH:
        return fetch_all_from_github()
    else:
        # Original implementation for local files
        if not CULTURES_DIR.exists():
            # If local files don't exist, fetch from GitHub
            return fetch_all_from_github()
        
        cultures = []
        for culture_dir in CULTURES_DIR.iterdir():
            if culture_dir.is_dir():
                # Try to load basic data to ensure it's a valid culture
                basic_data = load_culture_data(culture_dir.name)
                if basic_data:
                    cultures.append(basic_data)
        
        # Sort cultures by name
        cultures.sort(key=lambda x: x['name'])
        return cultures


def get_culture_names():
    """Get a simple list of culture names."""
    if not CULTURES_DIR.exists():
        return []
    
    culture_names = []
    for culture_dir in CULTURES_DIR.iterdir():
        if culture_dir.is_dir():
            culture_names.append(culture_dir.name)
    
    culture_names.sort()
    return culture_names


@app.route('/')
def index():
    """Main page displaying all cultures."""
    cultures = get_all_cultures()
    return render_template('index.html', cultures=cultures)


@app.route('/culture/<culture_name>')
def culture_detail(culture_name):
    """Display detailed information about a specific culture."""
    culture_data = load_culture_data(culture_name)
    
    if not culture_data:
        return render_template('error.html', message="Culture not found"), 404
    
    all_cultures = get_culture_names()
    return render_template('culture_detail.html', culture=culture_data, all_cultures=all_cultures)


@app.route('/update-from-github')
def update_from_github():
    """Refresh data by fetching from GitHub."""
    from github_fetcher import fetch_all_cultures as fetch_all_from_github
    try:
        # This just tests the connection to GitHub
        cultures = fetch_all_from_github()
        return jsonify({
            "status": "success", 
            "message": f"Successfully fetched {len(cultures)} cultures from GitHub",
            "cultures_count": len(cultures)
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error fetching from GitHub: {str(e)}"
        }), 500


@app.route('/api/cultures')
def api_cultures():
    """API endpoint to get all cultures as JSON."""
    return jsonify(get_all_cultures())


@app.route('/api/culture/<culture_name>')
def api_culture(culture_name):
    """API endpoint to get a specific culture as JSON."""
    culture_data = load_culture_data(culture_name)
    
    if not culture_data:
        return jsonify({"error": "Culture not found"}), 404
    
    return jsonify(culture_data)


@app.route('/compare')
def compare():
    """Page to compare two cultures."""
    all_cultures = get_culture_names()
    return render_template('compare.html', all_cultures=all_cultures)


@app.route('/api/compare/<culture1>/<culture2>')
def api_compare(culture1, culture2):
    """API endpoint to compare two cultures."""
    data1 = load_culture_data(culture1)
    data2 = load_culture_data(culture2)
    
    if not data1 or not data2:
        return jsonify({"error": "One or both cultures not found"}), 404
    
    comparison = {
        "culture1": data1,
        "culture2": data2,
        "similarities": find_similarities(data1, data2),
        "differences": find_differences(data1, data2)
    }
    
    return jsonify(comparison)


@app.route('/settings')
def settings():
    """Settings page for user preferences."""
    cultures = get_culture_names()
    return render_template('settings.html', all_cultures=cultures)


@app.route('/api/settings', methods=['POST'])
def api_settings():
    """API endpoint to save user settings."""
    settings = request.json
    # In a real implementation, you might save these to a database or user profile
    return jsonify({"status": "success", "message": "Settings saved successfully"})


@app.route('/api/theme', methods=['POST'])
def api_theme():
    """API endpoint to change theme."""
    theme = request.json.get('theme', 'light')
    # In a real implementation, you might save this to user preferences
    return jsonify({"status": "success", "theme": theme})


def find_similarities(culture1, culture2):
    """Find similarities between two cultures."""
    similarities = []
    
    # Compare core values
    if 'values' in culture1 and 'values' in culture2:
        values1 = set(culture1['values'].get('core_values', []))
        values2 = set(culture2['values'].get('core_values', []))
        common_values = values1.intersection(values2)
        if common_values:
            similarities.append({
                "type": "core_values",
                "items": list(common_values),
                "description": "Shared core values"
            })
    
    # Compare innovations
    if 'innovations_html' in culture1 and 'innovations_html' in culture2:
        # This is a simple comparison - in a full implementation, 
        # you might want to parse the markdown to extract innovations
        pass  # Placeholder for more sophisticated comparison
    
    return similarities


def find_differences(culture1, culture2):
    """Find differences between two cultures."""
    differences = []
    
    # Differences in time periods
    readme1 = culture1.get('readme_raw', '')
    readme2 = culture2.get('readme_raw', '')
    
    # Simple extraction of time periods from READMEs
    time_period1 = "Time period not specified"
    time_period2 = "Time period not specified"
    
    for line in readme1.split('\n'):
        if 'Time Period:' in line:
            time_period1 = line.replace('**Time Period:**', '').strip()
            break
    
    for line in readme2.split('\n'):
        if 'Time Period:' in line:
            time_period2 = line.replace('**Time Period:**', '').strip()
            break
    
    if time_period1 != time_period2:
        differences.append({
            "type": "time_period",
            "culture1_value": time_period1,
            "culture2_value": time_period2,
            "description": "Different time periods"
        })
    
    return differences


@app.route('/timeline')
def timeline():
    """Visual timeline of all cultures."""
    cultures = get_all_cultures()
    
    # Prepare timeline data
    timeline_events = []
    for culture in cultures:
        readme = culture.get('readme_raw', '')
        time_period = "Unknown"
        geography = "Unknown"
        
        # Extract time period and geography from README
        for line in readme.split('\n'):
            if 'Time Period:' in line:
                time_period = line.replace('**Time Period:**', '').replace('**', '').strip()
            elif 'Geography:' in line:
                geography = line.replace('**Geography:**', '').replace('**', '').strip()
        
        # Extract the earliest and latest dates from timeline events if available
        start_date = None
        end_date = None
        
        if 'timeline' in culture:
            for event in culture['timeline']:
                date_str = event.get('date', '')
                # Simple attempt to extract the year
                import re
                # This pattern captures the year before CE/BCE/BC/AD
                years = re.findall(r'([0-9]+)\s*(?:BCE|BC|CE|AD)', date_str)
                # Also try to match just a year without a period indicator
                if not years:
                    years = re.findall(r'^([0-9]+)', date_str.split()[0] if date_str.split() else '')
                
                if years:
                    year = int(years[0])
                    if 'BCE' in date_str or 'BC' in date_str:
                        year = -year
                    
                    if start_date is None or year < start_date:
                        start_date = year
                    if end_date is None or year > end_date:
                        end_date = year
        
        timeline_events.append({
            'name': culture['name'],
            'time_period': time_period,
            'geography': geography,
            'start_date': start_date,
            'end_date': end_date
        })
    
    return render_template('timeline.html', timeline_events=timeline_events)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)