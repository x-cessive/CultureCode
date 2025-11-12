#!/bin/bash

# culture.sh - CLI interface for the CultureCode project
# Provides commands to interact with cultural data

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
OUTPUT_FORMAT="markdown"
CULTURES_DIR="cultures"

# Function to print usage information
usage() {
    echo "Usage: $0 [command] [options]"
    echo ""
    echo "Commands:"
    echo "  list                    List all available cultures"
    echo "  info <culture>          Display information about a specific culture"
    echo "  compare <culture1> <culture2>  Compare two cultures"
    echo "  diff <culture1> <culture2>     Show differences between two cultures"
    echo "  timeline <culture>      Show the timeline of a culture"
    echo "  dependencies <culture>  Show cultural dependencies"
    echo "  search <term>           Search for a term across all cultures"
    echo "  lineage                 Generate cultural lineage graph"
    echo "  help                    Display this help message"
    echo ""
    echo "Examples:"
    echo "  $0 list"
    echo "  $0 info Egypt_Ancient"
    echo "  $0 compare Egypt_Ancient Greece_Classical"
    echo "  $0 search 'democracy'"
}

# Function to list all cultures
list_cultures() {
    echo -e "${BLUE}Available cultures:${NC}"
    if [ -d "$CULTURES_DIR" ]; then
        for dir in "$CULTURES_DIR"/*/; do
            if [ -d "$dir" ]; then
                basename "$dir"
            fi
        done
    else
        echo "No cultures directory found."
    fi
}

# Function to show info about a culture
info_culture() {
    local culture=$1
    local culture_path="$CULTURES_DIR/$culture"
    
    if [ ! -d "$culture_path" ]; then
        echo -e "${RED}Error: Culture '$culture' not found.${NC}" >&2
        return 1
    fi
    
    echo -e "${BLUE}Information about $culture:${NC}"
    
    # Show README if it exists
    if [ -f "$culture_path/README.md" ]; then
        echo -e "${GREEN}README:${NC}"
        head -20 "$culture_path/README.md"
        echo "..."
    fi
    
    # Show core values if they exist
    if [ -f "$culture_path/values.yaml" ]; then
        echo -e "${GREEN}Core Values:${NC}"
        grep -A 10 "core_values:" "$culture_path/values.yaml" | tail -n +2
    fi
}

# Function to compare two cultures
compare_cultures() {
    local culture1=$1
    local culture2=$2
    
    if [ ! -d "$CULTURES_DIR/$culture1" ] || [ ! -d "$CULTURES_DIR/$culture2" ]; then
        echo -e "${RED}Error: One or both cultures not found.${NC}" >&2
        return 1
    fi
    
    echo -e "${BLUE}Comparing $culture1 vs $culture2:${NC}"
    
    # Use the Python compare script if available
    if [ -f "tools/compare.py" ]; then
        python3 tools/compare.py "$culture1" "$culture2"
    else
        echo "Compare tool not available. Please ensure tools/compare.py exists."
    fi
}

# Function to show timeline of a culture
show_timeline() {
    local culture=$1
    local culture_path="$CULTURES_DIR/$culture"
    
    if [ ! -d "$culture_path" ]; then
        echo -e "${RED}Error: Culture '$culture' not found.${NC}" >&2
        return 1
    fi
    
    if [ -f "$culture_path/timeline.json" ]; then
        echo -e "${BLUE}Timeline for $culture:${NC}"
        jq -r '.[] | "\(.date): \(.event) - \(.commit_message)"' "$culture_path/timeline.json"
    else
        echo "Timeline file not found for $culture."
    fi
}

# Function to show dependencies of a culture
show_dependencies() {
    local culture=$1
    local culture_path="$CULTURES_DIR/$culture"
    
    if [ ! -d "$culture_path" ]; then
        echo -e "${RED}Error: Culture '$culture' not found.${NC}" >&2
        return 1
    fi
    
    if [ -f "$culture_path/dependencies.json" ]; then
        echo -e "${BLUE}Dependencies for $culture:${NC}"
        echo "Imports (influences from):"
        jq -r '.imports[]?' "$culture_path/dependencies.json"
        echo "Exports (influences to):"
        jq -r '.exports[]?' "$culture_path/dependencies.json"
        echo "Forks:"
        jq -r '.forks[]?' "$culture_path/dependencies.json"
    else
        echo "Dependencies file not found for $culture."
    fi
}

# Function to search for a term across cultures
search_term() {
    local term=$1
    echo -e "${BLUE}Searching for '$term' across cultures:${NC}"
    
    if [ -d "$CULTURES_DIR" ]; then
        grep -r -i -n -H "$term" "$CULTURES_DIR/" --include="*.md" --include="*.json" --include="*.yaml" --include="*.txt"
    fi
}

# Function to generate lineage graph
generate_lineage() {
    echo -e "${BLUE}Generating cultural lineage graph...${NC}"
    
    if [ -f "tools/lineage_graph.py" ]; then
        python3 tools/lineage_graph.py
    else
        echo "Lineage graph tool not available. Please ensure tools/lineage_graph.py exists."
    fi
}

# Main command processing
case "${1:-help}" in
    list)
        list_cultures
        ;;
    info)
        if [ -z "$2" ]; then
            echo -e "${RED}Error: Please specify a culture name.${NC}" >&2
            exit 1
        fi
        info_culture "$2"
        ;;
    compare|diff)
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo -e "${RED}Error: Please specify two culture names.${NC}" >&2
            exit 1
        fi
        compare_cultures "$2" "$3"
        ;;
    timeline)
        if [ -z "$2" ]; then
            echo -e "${RED}Error: Please specify a culture name.${NC}" >&2
            exit 1
        fi
        show_timeline "$2"
        ;;
    dependencies)
        if [ -z "$2" ]; then
            echo -e "${RED}Error: Please specify a culture name.${NC}" >&2
            exit 1
        fi
        show_dependencies "$2"
        ;;
    search)
        if [ -z "$2" ]; then
            echo -e "${RED}Error: Please specify a search term.${NC}" >&2
            exit 1
        fi
        search_term "$2"
        ;;
    lineage)
        generate_lineage
        ;;
    help|"")
        usage
        ;;
    *)
        echo -e "${RED}Unknown command: $1${NC}" >&2
        usage
        exit 1
        ;;
esac