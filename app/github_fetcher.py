"""
GitHub Data Fetcher for CultureCode
Fetches culture data directly from the GitHub repository
"""

import json
import yaml
import requests
from pathlib import Path
import markdown

# GitHub repository information
GITHUB_REPO = "x-cessive/CultureCode"
GITHUB_API_BASE = f"https://api.github.com/repos/{GITHUB_REPO}"

def fetch_file_from_github(file_path):
    """
    Fetch a file directly from GitHub repository
    """
    url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main/{file_path}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching {file_path}: {response.status_code}")
        return None


def fetch_culture_list():
    """
    Fetch the list of cultures by getting the directory listing from GitHub
    """
    # For this implementation, we'll use a known list of cultures
    # In a more advanced implementation, you could use the GitHub API 
    # to get the actual directory listing
    return [
        "Egypt_Ancient",
        "Greece_Classical", 
        "Rome",
        "Han_China",
        "Maya",
        "Islamic_Golden_Age",
        "Medieval_Europe",
        "Mali_Empire"
    ]


def fetch_culture_data(culture_name):
    """
    Fetch all data for a specific culture from GitHub
    """
    data = {"name": culture_name, "directory": culture_name}
    
    # Fetch README
    readme_content = fetch_file_from_github(f"cultures/{culture_name}/README.md")
    if readme_content:
        data['readme_raw'] = readme_content
        data['readme_html'] = markdown.markdown(readme_content)
    
    # Fetch values
    values_content = fetch_file_from_github(f"cultures/{culture_name}/values.yaml")
    if values_content:
        try:
            data['values'] = yaml.safe_load(values_content)
        except yaml.YAMLError:
            data['values'] = {}
    
    # Fetch social systems
    social_content = fetch_file_from_github(f"cultures/{culture_name}/social_systems.md")
    if social_content:
        data['social_systems_raw'] = social_content
        data['social_systems_html'] = markdown.markdown(social_content)
    
    # Fetch innovations
    innovations_content = fetch_file_from_github(f"cultures/{culture_name}/innovations.md")
    if innovations_content:
        data['innovations_raw'] = innovations_content
        data['innovations_html'] = markdown.markdown(innovations_content)
    
    # Fetch timeline
    timeline_content = fetch_file_from_github(f"cultures/{culture_name}/timeline.json")
    if timeline_content:
        try:
            data['timeline'] = json.loads(timeline_content)
        except json.JSONDecodeError:
            data['timeline'] = []
    
    # Fetch dependencies
    dependencies_content = fetch_file_from_github(f"cultures/{culture_name}/dependencies.json")
    if dependencies_content:
        try:
            data['dependencies'] = json.loads(dependencies_content)
        except json.JSONDecodeError:
            data['dependencies'] = {}
    
    return data


def fetch_all_cultures():
    """
    Fetch data for all cultures
    """
    culture_names = fetch_culture_list()
    cultures = []
    
    for culture_name in culture_names:
        culture_data = fetch_culture_data(culture_name)
        if culture_data:  # Only add if we were able to fetch data
            cultures.append(culture_data)
    
    # Sort cultures by name
    cultures.sort(key=lambda x: x['name'])
    return cultures