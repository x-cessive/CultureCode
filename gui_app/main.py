"""
The Hitchhiker's Guide to History - Desktop GUI Application
A tkinter-based application to explore the CultureCode repository
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import json
import yaml
import os
from pathlib import Path
import markdown
import webbrowser
import requests
import threading
from PIL import Image, ImageTk


class CultureCodeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("The Hitchhiker's Guide to History")
        self.root.geometry("1000x700")
        
        # Configuration
        self.USE_GITHUB_FETCH = False  # Default to local files
        self.CULTURES_DIR = Path(__file__).parent.parent / "cultures"
        
        # Initialize data
        self.cultures = []
        self.current_culture = None
        
        # Create the UI
        self.create_widgets()
        
        # Load cultures
        self.load_cultures()
        
        # Select first culture by default
        if self.cultures:
            self.culture_listbox.selection_set(0)
            self.on_culture_select(None)
    
    def create_widgets(self):
        # Create main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create menu bar
        self.create_menu()
        
        # Create main layout with paned window
        paned_window = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Culture list
        left_frame = ttk.Frame(paned_window)
        paned_window.add(left_frame, weight=1)
        
        ttk.Label(left_frame, text="Available Cultures:", font=("Arial", 12, "bold")).pack(anchor=tk.W, pady=(0, 5))
        
        # Culture listbox with scrollbar
        list_frame = ttk.Frame(left_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        self.culture_listbox = tk.Listbox(list_frame)
        culture_scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.culture_listbox.yview)
        self.culture_listbox.configure(yscrollcommand=culture_scrollbar.set)
        
        self.culture_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        culture_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.culture_listbox.bind('<<ListboxSelect>>', self.on_culture_select)
        
        # Right panel - Culture details
        right_frame = ttk.Frame(paned_window)
        paned_window.add(right_frame, weight=3)
        
        # Culture details notebook
        self.notebook = ttk.Notebook(right_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Overview tab
        self.overview_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.overview_frame, text="Overview")
        
        self.overview_text = scrolledtext.ScrolledText(self.overview_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.overview_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Values tab
        self.values_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.values_frame, text="Core Values")
        
        self.values_text = scrolledtext.ScrolledText(self.values_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.values_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Social Systems tab
        self.social_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.social_frame, text="Social Systems")
        
        self.social_text = scrolledtext.ScrolledText(self.social_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.social_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Innovations tab
        self.innovations_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.innovations_frame, text="Innovations")
        
        self.innovations_text = scrolledtext.ScrolledText(self.innovations_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.innovations_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Timeline tab
        self.timeline_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.timeline_frame, text="Timeline")
        
        self.timeline_text = scrolledtext.ScrolledText(self.timeline_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.timeline_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Dependencies tab
        self.dependencies_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.dependencies_frame, text="Dependencies")
        
        self.dependencies_text = scrolledtext.ScrolledText(self.dependencies_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.dependencies_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Refresh from GitHub", command=self.refresh_from_github)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Compare Cultures", command=self.open_compare_window)
        tools_menu.add_command(label="View Timeline", command=self.open_timeline_window)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
    
    def load_cultures(self):
        """Load culture names and populate the listbox"""
        self.cultures = self.get_culture_names()
        
        # Clear the listbox
        self.culture_listbox.delete(0, tk.END)
        
        # Add cultures to the listbox
        for culture in self.cultures:
            self.culture_listbox.insert(tk.END, culture.replace('_', ' '))
    
    def get_culture_names(self):
        """Get a list of culture names from the cultures directory"""
        if not self.CULTURES_DIR.exists():
            return []
        
        culture_names = []
        for culture_dir in self.CULTURES_DIR.iterdir():
            if culture_dir.is_dir():
                # Check if it has the necessary files to be considered a culture
                required_files = ["README.md", "values.yaml", "social_systems.md", 
                                 "innovations.md", "timeline.json", "dependencies.json"]
                has_all_files = all((culture_dir / file).exists() for file in required_files)
                
                if has_all_files:
                    culture_names.append(culture_dir.name)
        
        culture_names.sort()
        return culture_names
    
    def on_culture_select(self, event):
        """Handle culture selection from the listbox"""
        selection = self.culture_listbox.curselection()
        if not selection:
            return
        
        index = selection[0]
        culture_name = self.cultures[index]
        self.current_culture = culture_name
        
        # Load culture data and display in tabs
        culture_data = self.load_culture_data(culture_name)
        
        if culture_data:
            self.display_culture_data(culture_data)
    
    def load_culture_data(self, culture_name):
        """Load culture data from local files"""
        culture_path = self.CULTURES_DIR / culture_name
        
        if not culture_path.exists():
            return None
        
        data = {"name": culture_name, "directory": culture_name}
        
        # Load README
        readme_path = culture_path / "README.md"
        if readme_path.exists():
            with open(readme_path, 'r', encoding='utf-8') as f:
                data['readme_raw'] = f.read()
                # Convert markdown to plain text for display
                data['readme_html'] = f.read()
        
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
        
        # Load innovations
        innovations_path = culture_path / "innovations.md"
        if innovations_path.exists():
            with open(innovations_path, 'r', encoding='utf-8') as f:
                data['innovations_raw'] = f.read()
        
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
        
        # Extract key information from README for easy access
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
        
        return data
    
    def display_culture_data(self, culture_data):
        """Display culture data in the appropriate tabs"""
        # Display Overview
        self.overview_text.config(state=tk.NORMAL)
        self.overview_text.delete(1.0, tk.END)
        
        if 'readme_raw' in culture_data:
            readme = culture_data['readme_raw']
            self.overview_text.insert(tk.END, f"Culture: {culture_data['name'].replace('_', ' ')}\n\n")
            self.overview_text.insert(tk.END, f"Time Period: {culture_data.get('time_period', 'Time period not specified')}\n")
            self.overview_text.insert(tk.END, f"Geography: {culture_data.get('geography', 'Geography not specified')}\n\n")
            self.overview_text.insert(tk.END, readme)
        else:
            self.overview_text.insert(tk.END, f"No overview available for {culture_data['name']}")
        
        self.overview_text.config(state=tk.DISABLED)
        
        # Display Core Values
        self.values_text.config(state=tk.NORMAL)
        self.values_text.delete(1.0, tk.END)
        
        if 'values' in culture_data and culture_data['values']:
            values = culture_data['values']
            self.values_text.insert(tk.END, f"Core Values:\n")
            for value in values.get('core_values', []):
                self.values_text.insert(tk.END, f"• {value}\n")
            
            self.values_text.insert(tk.END, f"\nWorldview:\n")
            for worldview in values.get('worldview', []):
                self.values_text.insert(tk.END, f"• {worldview}\n")
            
            self.values_text.insert(tk.END, f"\nIdentity:\n")
            for identity in values.get('identity', []):
                self.values_text.insert(tk.END, f"• {identity}\n")
        else:
            self.values_text.insert(tk.END, "No values data available.")
        
        self.values_text.config(state=tk.DISABLED)
        
        # Display Social Systems
        self.social_text.config(state=tk.NORMAL)
        self.social_text.delete(1.0, tk.END)
        
        if 'social_systems_raw' in culture_data:
            self.social_text.insert(tk.END, culture_data['social_systems_raw'])
        else:
            self.social_text.insert(tk.END, "No social systems data available.")
        
        self.social_text.config(state=tk.DISABLED)
        
        # Display Innovations
        self.innovations_text.config(state=tk.NORMAL)
        self.innovations_text.delete(1.0, tk.END)
        
        if 'innovations_raw' in culture_data:
            self.innovations_text.insert(tk.END, culture_data['innovations_raw'])
        else:
            self.innovations_text.insert(tk.END, "No innovations data available.")
        
        self.innovations_text.config(state=tk.DISABLED)
        
        # Display Timeline
        self.timeline_text.config(state=tk.NORMAL)
        self.timeline_text.delete(1.0, tk.END)
        
        if 'timeline' in culture_data:
            for event in culture_data['timeline']:
                self.timeline_text.insert(tk.END, f"{event['date']}: {event['event']}\n")
                self.timeline_text.insert(tk.END, f"  Commit: {event['commit_message']}\n\n")
        else:
            self.timeline_text.insert(tk.END, "No timeline data available.")
        
        self.timeline_text.config(state=tk.DISABLED)
        
        # Display Dependencies
        self.dependencies_text.config(state=tk.NORMAL)
        self.dependencies_text.delete(1.0, tk.END)
        
        if 'dependencies' in culture_data:
            deps = culture_data['dependencies']
            
            self.dependencies_text.insert(tk.END, "Imports (Cultural Influences):\n")
            for imp in deps.get('imports', []):
                self.dependencies_text.insert(tk.END, f"• {imp}\n")
            
            self.dependencies_text.insert(tk.END, f"\nExports (Influences to Other Cultures):\n")
            for exp in deps.get('exports', []):
                self.dependencies_text.insert(tk.END, f"• {exp}\n")
            
            self.dependencies_text.insert(tk.END, f"\nForks (Successor Cultures):\n")
            for fork in deps.get('forks', []):
                self.dependencies_text.insert(tk.END, f"• {fork}\n")
        else:
            self.dependencies_text.insert(tk.END, "No dependencies data available.")
        
        self.dependencies_text.config(state=tk.DISABLED)
    
    def refresh_from_github(self):
        """Placeholder for refreshing data from GitHub"""
        def do_refresh():
            try:
                # In a real implementation, this would fetch data from GitHub
                # For now, we'll just reload the local data
                self.load_cultures()
                messagebox.showinfo("Refresh", "Data refreshed successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error refreshing data: {str(e)}")
        
        # Run in a separate thread to avoid blocking the UI
        threading.Thread(target=do_refresh, daemon=True).start()
    
    def open_compare_window(self):
        """Open a new window for comparing cultures"""
        CompareWindow(self.root, self.cultures, self)
    
    def open_timeline_window(self):
        """Open a timeline visualization window"""
        TimelineWindow(self.root, self.cultures, self)
    
    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo("About", "The Hitchhiker's Guide to History\n\n"
                            "A CultureCode project that treats culture like code, "
                            "documenting, forking, version-controlling, and "
                            "collaboratively exploring the evolution of human societies.")


class CompareWindow:
    def __init__(self, parent, cultures, main_app):
        self.main_app = main_app
        self.window = tk.Toplevel(parent)
        self.window.title("Compare Cultures")
        self.window.geometry("800x600")
        
        self.cultures = cultures
        
        # Create widgets
        self.create_widgets()
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Top frame for selection
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 10))
        
        # First culture selection
        first_frame = ttk.LabelFrame(top_frame, text="First Culture")
        first_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        self.first_var = tk.StringVar()
        self.first_combo = ttk.Combobox(first_frame, textvariable=self.first_var, state="readonly")
        self.first_combo['values'] = [c.replace('_', ' ') for c in self.cultures]
        self.first_combo.pack(fill=tk.X, padx=5, pady=5)
        self.first_combo.bind('<<ComboboxSelected>>', self.on_selection_change)
        
        # Second culture selection
        second_frame = ttk.LabelFrame(top_frame, text="Second Culture")
        second_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5, 0))
        
        self.second_var = tk.StringVar()
        self.second_combo = ttk.Combobox(second_frame, textvariable=self.second_var, state="readonly")
        self.second_combo['values'] = [c.replace('_', ' ') for c in self.cultures]
        self.second_combo.pack(fill=tk.X, padx=5, pady=5)
        self.second_combo.bind('<<ComboboxSelected>>', self.on_selection_change)
        
        # Notebook for comparison
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.overview_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.overview_tab, text="Overview Comparison")
        
        self.values_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.values_tab, text="Values Comparison")
        
        self.innovations_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.innovations_tab, text="Innovations Comparison")
        
        # Scrolled text widgets
        self.overview_text = scrolledtext.ScrolledText(self.overview_tab, wrap=tk.WORD)
        self.overview_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.values_text = scrolledtext.ScrolledText(self.values_tab, wrap=tk.WORD)
        self.values_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.innovations_text = scrolledtext.ScrolledText(self.innovations_tab, wrap=tk.WORD)
        self.innovations_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def on_selection_change(self, event):
        """Update comparison when selections change"""
        first_name = self.first_var.get().replace(' ', '_')
        second_name = self.second_var.get().replace(' ', '_')
        
        if first_name and second_name and first_name in self.cultures and second_name in self.cultures:
            # Load both cultures
            first_data = self.main_app.load_culture_data(first_name)
            second_data = self.main_app.load_culture_data(second_name)
            
            if first_data and second_data:
                self.update_comparison(first_data, second_data)
    
    def update_comparison(self, first_data, second_data):
        """Update the comparison tabs with culture data"""
        # Update Overview Comparison
        self.overview_text.config(state=tk.NORMAL)
        self.overview_text.delete(1.0, tk.END)
        
        first_name = first_data['name'].replace('_', ' ')
        second_name = second_data['name'].replace('_', ' ')
        
        self.overview_text.insert(tk.END, f"Comparison: {first_name} vs {second_name}\n\n")
        
        # Time periods
        self.overview_text.insert(tk.END, f"{first_name} Time Period: {first_data.get('time_period', 'Time period not specified')}\n")
        self.overview_text.insert(tk.END, f"{second_name} Time Period: {second_data.get('time_period', 'Time period not specified')}\n\n")
        
        # Geographies
        self.overview_text.insert(tk.END, f"{first_name} Geography: {first_data.get('geography', 'Geography not specified')}\n")
        self.overview_text.insert(tk.END, f"{second_name} Geography: {second_data.get('geography', 'Geography not specified')}\n\n")
        
        self.overview_text.config(state=tk.DISABLED)
        
        # Update Values Comparison
        self.values_text.config(state=tk.NORMAL)
        self.values_text.delete(1.0, tk.END)
        
        self.values_text.insert(tk.END, f"Core Values Comparison: {first_name} vs {second_name}\n\n")
        
        first_values = set(first_data.get('values', {}).get('core_values', []))
        second_values = set(second_data.get('values', {}).get('core_values', []))
        
        common_values = first_values.intersection(second_values)
        first_only_values = first_values.difference(second_values)
        second_only_values = second_values.difference(first_values)
        
        if common_values:
            self.values_text.insert(tk.END, f"Common Values:\n")
            for val in common_values:
                self.values_text.insert(tk.END, f"  • {val}\n")
            self.values_text.insert(tk.END, f"\n")
        
        if first_only_values:
            self.values_text.insert(tk.END, f"{first_name} Only Values:\n")
            for val in first_only_values:
                self.values_text.insert(tk.END, f"  • {val}\n")
            self.values_text.insert(tk.END, f"\n")
        
        if second_only_values:
            self.values_text.insert(tk.END, f"{second_name} Only Values:\n")
            for val in second_only_values:
                self.values_text.insert(tk.END, f"  • {val}\n")
            self.values_text.insert(tk.END, f"\n")
        
        self.values_text.config(state=tk.DISABLED)
        
        # Update Innovations Comparison
        self.innovations_text.config(state=tk.NORMAL)
        self.innovations_text.delete(1.0, tk.END)
        
        self.innovations_text.insert(tk.END, f"Innovations Comparison: {first_name} vs {second_name}\n\n")
        
        self.innovations_text.config(state=tk.DISABLED)


class TimelineWindow:
    def __init__(self, parent, cultures, main_app):
        self.main_app = main_app
        self.window = tk.Toplevel(parent)
        self.window.title("Cultural Timeline")
        self.window.geometry("900x700")
        
        self.cultures = cultures
        
        # Create widgets
        self.create_widgets()
        self.load_timeline_data()
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.window)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Canvas for timeline visualization
        canvas_frame = ttk.Frame(main_frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(canvas_frame, bg="white")
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def load_timeline_data(self):
        """Load timeline data for all cultures"""
        all_events = []
        
        for culture_name in self.cultures:
            culture_data = self.main_app.load_culture_data(culture_name)
            if culture_data and 'timeline' in culture_data:
                for event in culture_data['timeline']:
                    # Parse date to extract year (simplified)
                    date_str = event.get('date', '')
                    year = self.extract_year(date_str)
                    
                    if year is not None:
                        all_events.append({
                            'year': year,
                            'date': date_str,
                            'event': event.get('event', ''),
                            'culture': culture_name,
                            'commit': event.get('commit_message', '')
                        })
        
        # Sort events by year
        all_events.sort(key=lambda x: x['year'])
        
        # Draw timeline
        self.draw_timeline(all_events)
    
    def extract_year(self, date_str):
        """Extract year from date string (simplified)"""
        import re
        # Look for years in the date string
        years = re.findall(r'(\d+)\s*(?:BCE|BC|CE|AD)?', date_str)
        if years:
            year = int(years[0])
            if 'BCE' in date_str or 'BC' in date_str:
                year = -year
            return year
        return None
    
    def draw_timeline(self, events):
        """Draw the timeline on the canvas"""
        # Clear canvas
        self.canvas.delete("all")
        
        # Calculate dimensions
        canvas_width = self.canvas.winfo_reqwidth()
        canvas_height = self.canvas.winfo_reqheight() or 800  # Default height if not calculated yet
        
        # Define timeline parameters
        start_year = min((e['year'] for e in events), default=0) - 100
        end_year = max((e['year'] for e in events), default=0) + 100
        
        # Draw timeline line
        timeline_y = 50
        self.canvas.create_line(50, timeline_y, canvas_width - 50, timeline_y, arrow=tk.LAST)
        
        # Draw events
        y_pos = timeline_y + 30
        for event in events[:50]:  # Limit to first 50 events to prevent overcrowding
            year = event['year']
            
            # Calculate x position based on year
            x_pos = 50 + ((year - start_year) / (end_year - start_year)) * (canvas_width - 100)
            
            # Draw event marker
            self.canvas.create_oval(x_pos-3, y_pos-3, x_pos+3, y_pos+3, fill="blue", outline="black")
            
            # Draw event label
            label = f"{event['date']}: {event['event'][:30]}..." if len(event['event']) > 30 else event['event']
            self.canvas.create_text(x_pos, y_pos + 20, text=label, anchor=tk.N, width=150)
            
            y_pos += 40  # Move to next line
            
            # Reset position if we go too far down
            if y_pos > canvas_height - 100:
                y_pos = timeline_y + 30


def main():
    root = tk.Tk()
    app = CultureCodeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()