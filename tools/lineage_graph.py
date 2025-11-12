#!/usr/bin/env python3
"""
lineage_graph.py - Generate network graphs showing cultural influence
"""

import json
import argparse
import sys
from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt


def load_all_cultures():
    """Load all culture dependencies to build the lineage graph."""
    cultures_dir = Path("cultures")
    all_cultures = {}
    
    if not cultures_dir.exists():
        print("Error: cultures directory not found")
        return {}
    
    for culture_dir in cultures_dir.iterdir():
        if culture_dir.is_dir():
            dependencies_path = culture_dir / "dependencies.json"
            if dependencies_path.exists():
                with open(dependencies_path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        all_cultures[culture_dir.name] = data
                    except json.JSONDecodeError:
                        print(f"Error: Invalid JSON in {dependencies_path}")
    
    return all_cultures


def create_lineage_graph(cultures_data):
    """Create a directed graph showing cultural influence."""
    G = nx.DiGraph()
    
    # Add nodes for each culture
    for culture_name in cultures_data:
        G.add_node(culture_name)
    
    # Add edges based on dependencies
    for culture_name, data in cultures_data.items():
        dependencies = data.get('dependencies', {})
        
        # Add edges from imports (this culture was influenced by these)
        for imported_culture in dependencies.get('imports', []):
            if imported_culture in cultures_data:
                G.add_edge(imported_culture, culture_name, relation='influence')
        
        # Add edges to exports (this culture influenced these)
        for exported_culture in dependencies.get('exports', []):
            if exported_culture in cultures_data:
                G.add_edge(culture_name, exported_culture, relation='influence')
        
        # Add edges for forks (this culture split into these)
        for forked_culture in dependencies.get('forks', []):
            if forked_culture in cultures_data:
                G.add_edge(culture_name, forked_culture, relation='fork')
    
    return G


def visualize_graph(G, output_file="cultural_lineage.png"):
    """Visualize the cultural lineage graph."""
    plt.figure(figsize=(12, 8))
    
    # Create a layout for the graph
    pos = nx.spring_layout(G, k=2, iterations=50)
    
    # Draw the nodes
    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='lightblue', alpha=0.9)
    
    # Draw the labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    
    # Draw the edges
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray', arrows=True)
    
    # Add title
    plt.title("Cultural Lineage Graph", size=15)
    
    # Remove axes
    plt.axis('off')
    
    # Save the graph
    plt.savefig(output_file, format="png", bbox_inches="tight")
    print(f"Graph saved as {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Generate a visual graph of cultural influences')
    parser.add_argument('--output', '-o', default='cultural_lineage.png', 
                        help='Output filename for the graph image')
    parser.add_argument('--format', '-f', choices=['png', 'pdf', 'svg'], default='png',
                        help='Output format for the graph image')
    
    args = parser.parse_args()
    
    # Load all cultures
    cultures_data = load_all_cultures()
    
    if not cultures_data:
        print("No cultural data found to create lineage graph")
        sys.exit(1)
    
    # Create the lineage graph
    G = create_lineage_graph(cultures_data)
    
    # Visualize the graph with appropriate format
    output_file = f"cultural_lineage.{args.format}"
    visualize_graph(G, output_file)


if __name__ == "__main__":
    main()