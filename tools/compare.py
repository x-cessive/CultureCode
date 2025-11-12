#!/usr/bin/env python3
"""
compare.py - Compare two cultures and output their differences
"""

import json
import yaml
import argparse
import sys
from pathlib import Path


def load_culture_data(culture_name):
    """Load culture data from the cultures directory."""
    culture_path = Path(f"cultures/{culture_name}")
    
    data = {}
    
    # Load README if it exists
    readme_path = culture_path / "README.md"
    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8') as f:
            data['readme'] = f.read()
    
    # Load values from YAML if it exists
    values_path = culture_path / "values.yaml"
    if values_path.exists():
        with open(values_path, 'r', encoding='utf-8') as f:
            data['values'] = yaml.safe_load(f)
    
    # Load social systems from markdown if it exists
    social_path = culture_path / "social_systems.md"
    if social_path.exists():
        with open(social_path, 'r', encoding='utf-8') as f:
            data['social_systems'] = f.read()
    
    # Load innovations from markdown if it exists
    innovations_path = culture_path / "innovations.md"
    if innovations_path.exists():
        with open(innovations_path, 'r', encoding='utf-8') as f:
            data['innovations'] = f.read()
    
    # Load timeline from JSON if it exists
    timeline_path = culture_path / "timeline.json"
    if timeline_path.exists():
        with open(timeline_path, 'r', encoding='utf-8') as f:
            data['timeline'] = json.load(f)
    
    # Load dependencies from JSON if it exists
    dependencies_path = culture_path / "dependencies.json"
    if dependencies_path.exists():
        with open(dependencies_path, 'r', encoding='utf-8') as f:
            data['dependencies'] = json.load(f)
    
    return data


def compare_values(culture1_data, culture2_data):
    """Compare core values between two cultures."""
    c1_values = set(culture1_data.get('values', {}).get('core_values', []))
    c2_values = set(culture2_data.get('values', {}).get('core_values', []))
    
    common = c1_values.intersection(c2_values)
    only_c1 = c1_values.difference(c2_values)
    only_c2 = c2_values.difference(c1_values)
    
    print("## Core Values Comparison\n")
    print(f"**Common values:** {', '.join(common) if common else 'None'}")
    print(f"**Only in {args.culture1}:** {', '.join(only_c1) if only_c1 else 'None'}")
    print(f"**Only in {args.culture2}:** {', '.join(only_c2) if only_c2 else 'None'}\n")


def compare_governments(culture1_data, culture2_data):
    """Compare government systems between two cultures."""
    c1_gov = culture1_data.get('social_systems.md', {}).get('government', 'Unknown')
    c2_gov = culture2_data.get('social_systems.md', {}).get('government', 'Unknown')
    
    print("## Government Comparison\n")
    print(f"**{args.culture1}:** {c1_gov}")
    print(f"**{args.culture2}:** {c2_gov}\n")


def compare_innovations(culture1_data, culture2_data):
    """Compare innovations between two cultures."""
    # Extract innovations from the markdown content
    c1_innovations_text = culture1_data.get('innovations', '')
    c2_innovations_text = culture2_data.get('innovations', '')
    
    # Parse innovations from markdown (simplified - just extract items after bullet points)
    import re
    
    # Find all items in the markdown that start with '- '
    c1_innovations_matches = re.findall(r'-\s+(.+)', c1_innovations_text)
    c2_innovations_matches = re.findall(r'-\s+(.+)', c2_innovations_text)
    
    c1_innovations = set(c1_innovations_matches)
    c2_innovations = set(c2_innovations_matches)
    
    common = c1_innovations.intersection(c2_innovations)
    only_c1 = c1_innovations.difference(c2_innovations)
    only_c2 = c2_innovations.difference(c1_innovations)
    
    print("## Innovation Comparison\n")
    print(f"**Common innovations:** {', '.join(common) if common else 'None'}")
    print(f"**Only in {args.culture1}:** {', '.join(only_c1) if only_c1 else 'None'}")
    print(f"**Only in {args.culture2}:** {', '.join(only_c2) if only_c2 else 'None'}\n")


def main():
    global args
    
    parser = argparse.ArgumentParser(description='Compare two cultures and output their differences')
    parser.add_argument('culture1', help='Name of the first culture to compare')
    parser.add_argument('culture2', help='Name of the second culture to compare')
    
    args = parser.parse_args()
    
    print(f"# Comparing {args.culture1} vs {args.culture2}\n")
    
    # Load data for both cultures
    try:
        culture1_data = load_culture_data(args.culture1)
        culture2_data = load_culture_data(args.culture2)
    except Exception as e:
        print(f"Error loading culture data: {e}")
        sys.exit(1)
    
    # Perform comparisons
    compare_values(culture1_data, culture2_data)
    compare_innovations(culture1_data, culture2_data)


if __name__ == "__main__":
    main()