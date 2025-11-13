"""
The Hitchhiker's Guide to History - Kivy Android Application
An Android version of the CultureCode project
"""

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.core.window import Window
from kivy.uix.widget import Widget
import json
import yaml
import os
from pathlib import Path
import requests
import threading


class CultureRV(RecycleView):
    def __init__(self, **kwargs):
        super(CultureRV, self).__init__(**kwargs)
        self.viewclass = 'Label'
        self.data = []


class CultureListScreen(Screen):
    def __init__(self, manager, **kwargs):
        super(CultureListScreen, self).__init__(**kwargs)
        self.manager = manager
        
        # Configuration
        self.CULTURES_DIR = Path(__file__).parent.parent / "cultures"  # Adjusted for Android packaging
        self.cultures = []
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(text='The Hitchhiker\'s Guide to History', size_hint_y=None, height=50, 
                      color=(0.2, 0.3, 0.8, 1), font_size=20)
        layout.add_widget(header)
        
        # Culture list
        self.culture_list = CultureRV(size_hint_y=0.8)
        layout.add_widget(self.culture_list)
        
        # Buttons
        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        select_btn = Button(text='Select Culture', size_hint_x=0.5)
        select_btn.bind(on_press=self.select_culture)
        button_layout.add_widget(select_btn)
        
        compare_btn = Button(text='Compare Cultures', size_hint_x=0.5)
        compare_btn.bind(on_press=self.open_compare)
        button_layout.add_widget(compare_btn)
        
        layout.add_widget(button_layout)
        
        # Load cultures
        self.load_cultures()
        
        self.add_widget(layout)
    
    def load_cultures(self):
        """Load culture names and populate the list"""
        # For Android, we'll try a different approach to locate the cultures directory
        # The cultures might be packaged with the app or accessed via a different path
        try:
            # Try various possible paths for the cultures directory
            possible_paths = [
                Path("cultures"),
                Path(__file__).parent / "cultures",
                Path(".") / "cultures", 
                Path("/storage/emulated/0/Documents/CultureCode/cultures"),  # For Android storage
            ]
            
            cultures_dir = None
            for p in possible_paths:
                if p.exists():
                    cultures_dir = p
                    break
            
            if cultures_dir is None:
                # If no local cultures found, use a placeholder
                self.cultures = [
                    {"name": "Egypt_Ancient", "text": "Ancient Egypt (3100 BCE – 30 BCE)"},
                    {"name": "Greece_Classical", "text": "Classical Greece (5th-4th centuries BCE)"},
                    {"name": "Rome", "text": "Ancient Rome (753 BCE – 476 CE)"},
                    {"name": "Han_China", "text": "Han Dynasty China (206 BCE – 220 CE)"},
                    {"name": "Maya", "text": "Maya Civilization (2000 BCE – 16th century CE)"},
                    {"name": "Islamic_Golden_Age", "text": "Islamic Golden Age (8th-13th centuries)"},
                    {"name": "Medieval_Europe", "text": "Medieval Europe (5th-15th centuries)"},
                    {"name": "Mali_Empire", "text": "Mali Empire (1235-1670 CE)"}
                ]
            else:
                self.cultures = []
                for culture_dir in cultures_dir.iterdir():
                    if culture_dir.is_dir():
                        required_files = ["README.md", "values.yaml", "social_systems.md", 
                                        "innovations.md", "timeline.json", "dependencies.json"]
                        has_all_files = all((culture_dir / file).exists() for file in required_files)
                        
                        if has_all_files:
                            culture_name = culture_dir.name
                            # Try to extract basic info from README
                            readme_path = culture_dir / "README.md"
                            description = "No description available"
                            
                            if readme_path.exists():
                                with open(readme_path, 'r', encoding='utf-8') as f:
                                    lines = f.read().split('\n')
                                    for line in lines:
                                        if 'Time Period:' in line:
                                            description = line.replace('**Time Period:**', '').replace('**', '').strip()
                                            break
                            
                            self.cultures.append({
                                "name": culture_name,
                                "text": f"{culture_name.replace('_', ' ')}: {description}"
                            })
            
            # Sort cultures
            self.cultures.sort(key=lambda x: x["name"])
            
            # Populate the recycle view
            self.culture_list.data = [{'text': c["text"], 'name': c["name"]} for c in self.cultures]
            
        except Exception as e:
            print(f"Error loading cultures: {e}")
            # Default to some example cultures
            self.cultures = [
                {"name": "Egypt_Ancient", "text": "Ancient Egypt (3100 BCE – 30 BCE)"},
                {"name": "Greece_Classical", "text": "Classical Greece (5th-4th centuries BCE)"},
                {"name": "Rome", "text": "Ancient Rome (753 BCE – 476 CE)"}
            ]
            self.culture_list.data = [{'text': c["text"], 'name': c["name"]} for c in self.cultures]

    def select_culture(self, instance):
        """Handle culture selection"""
        # Get the selected culture
        if self.culture_list.refresh_from_data():
            # For this example, we'll just show the first item if any selected
            selected_index = 0  # Simplified selection for demo purposes
            if 0 <= selected_index < len(self.cultures):
                culture_name = self.cultures[selected_index]["name"]
                self.manager.current = 'culture_detail'
                # Pass culture name to the detail screen
                detail_screen = self.manager.get_screen('culture_detail')
                detail_screen.load_culture(culture_name)
    
    def open_compare(self, instance):
        """Open the compare cultures screen"""
        self.manager.current = 'compare'


class CultureDetailScreen(Screen):
    def __init__(self, manager, **kwargs):
        super(CultureDetailScreen, self).__init__(**kwargs)
        self.manager = manager
        self.current_culture = None
        
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        self.header = Label(text='Culture Details', size_hint_y=None, height=50, 
                           color=(0.2, 0.3, 0.8, 1), font_size=20)
        layout.add_widget(self.header)
        
        # Create tabbed panel
        self.tab_panel = TabbedPanel(do_default_tab=False)
        
        # Overview tab
        overview_tab = TabbedPanelItem(text='Overview')
        self.overview_content = Label(text='Select a culture to view details', halign='left', valign='top')
        self.overview_content.bind(
            texture_size=lambda obj, value: setattr(obj, 'text_size', (obj.width, None)),
            width=lambda obj, value: setattr(obj, 'text_size', (value, None)))
        
        scroll_view = ScrollView()
        scroll_view.add_widget(self.overview_content)
        overview_tab.add_widget(scroll_view)
        self.tab_panel.add_widget(overview_tab)
        
        # Values tab
        values_tab = TabbedPanelItem(text='Core Values')
        self.values_content = Label(text='', halign='left', valign='top')
        self.values_content.bind(
            texture_size=lambda obj, value: setattr(obj, 'text_size', (obj.width, None)),
            width=lambda obj, value: setattr(obj, 'text_size', (value, None)))
        
        scroll_view2 = ScrollView()
        scroll_view2.add_widget(self.values_content)
        values_tab.add_widget(scroll_view2)
        self.tab_panel.add_widget(values_tab)
        
        # Social Systems tab
        social_tab = TabbedPanelItem(text='Social Systems')
        self.social_content = Label(text='', halign='left', valign='top')
        self.social_content.bind(
            texture_size=lambda obj, value: setattr(obj, 'text_size', (obj.width, None)),
            width=lambda obj, value: setattr(obj, 'text_size', (value, None)))
        
        scroll_view3 = ScrollView()
        scroll_view3.add_widget(self.social_content)
        social_tab.add_widget(scroll_view3)
        self.tab_panel.add_widget(social_tab)
        
        # Add the tab panel to the layout
        layout.add_widget(self.tab_panel)
        
        # Back button
        back_btn = Button(text='Back to List', size_hint_y=None, height=50)
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
    
    def load_culture(self, culture_name):
        """Load and display culture details"""
        self.current_culture = culture_name
        self.header.text = culture_name.replace('_', ' ')
        
        try:
            # For Android, we'll use the same approach as before
            # Try various possible paths for the cultures directory
            possible_paths = [
                Path("cultures"),
                Path(__file__).parent / "cultures", 
                Path(".") / "cultures",
                Path("/storage/emulated/0/Documents/CultureCode/cultures"),  # For Android storage
            ]
            
            cultures_dir = None
            for p in possible_paths:
                if p.exists():
                    cultures_dir = p
                    break
            
            if cultures_dir:
                culture_path = cultures_dir / culture_name
                
                # Load README
                readme_path = culture_path / "README.md"
                if readme_path.exists():
                    with open(readme_path, 'r', encoding='utf-8') as f:
                        readme = f.read()
                        self.overview_content.text = readme
                else:
                    self.overview_content.text = f"README not found for {culture_name}"
                
                # Load values
                values_path = culture_path / "values.yaml"
                if values_path.exists():
                    with open(values_path, 'r', encoding='utf-8') as f:
                        try:
                            values = yaml.safe_load(f)
                            values_text = "Core Values:\n"
                            for value in values.get('core_values', []):
                                values_text += f"• {value}\n"
                            
                            values_text += "\nWorldview:\n"
                            for worldview in values.get('worldview', []):
                                values_text += f"• {worldview}\n"
                            
                            values_text += "\nIdentity:\n"
                            for identity in values.get('identity', []):
                                values_text += f"• {identity}\n"
                            
                            self.values_content.text = values_text
                        except yaml.YAMLError:
                            self.values_content.text = "Error loading values data"
                else:
                    self.values_content.text = "Values file not found"
                
                # Load social systems
                social_path = culture_path / "social_systems.md"
                if social_path.exists():
                    with open(social_path, 'r', encoding='utf-8') as f:
                        self.social_content.text = f.read()
                else:
                    self.social_content.text = "Social systems file not found"
            else:
                # Fallback if cultures directory not found
                self.overview_content.text = f"Could not find cultures directory. Selected: {culture_name}"
                self.values_content.text = "Values not available"
                self.social_content.text = "Social systems not available"
                
        except Exception as e:
            self.overview_content.text = f"Error loading culture data: {str(e)}"
            self.values_content.text = "Error loading values"
            self.social_content.text = "Error loading social systems"
    
    def go_back(self, instance):
        """Go back to the culture list"""
        self.manager.current = 'culture_list'


class CompareScreen(Screen):
    def __init__(self, manager, **kwargs):
        super(CompareScreen, self).__init__(**kwargs)
        self.manager = manager
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(text='Compare Cultures', size_hint_y=None, height=50, 
                      color=(0.2, 0.3, 0.8, 1), font_size=20)
        layout.add_widget(header)
        
        # Culture selection
        selection_layout = BoxLayout(size_hint_y=None, height=100, spacing=10)
        
        # First culture spinner
        first_layout = BoxLayout(orientation='vertical')
        first_label = Label(text='First Culture:', size_hint_y=None, height=30)
        self.first_spinner = Spinner(
            text='Select Culture',
            values=['Egypt_Ancient', 'Greece_Classical', 'Rome', 'Han_China', 
                   'Maya', 'Islamic_Golden_Age', 'Medieval_Europe', 'Mali_Empire']
        )
        first_layout.add_widget(first_label)
        first_layout.add_widget(self.first_spinner)
        selection_layout.add_widget(first_layout)
        
        # Second culture spinner
        second_layout = BoxLayout(orientation='vertical')
        second_label = Label(text='Second Culture:', size_hint_y=None, height=30)
        self.second_spinner = Spinner(
            text='Select Culture', 
            values=['Egypt_Ancient', 'Greece_Classical', 'Rome', 'Han_China', 
                   'Maya', 'Islamic_Golden_Age', 'Medieval_Europe', 'Mali_Empire']
        )
        second_layout.add_widget(second_label)
        second_layout.add_widget(self.second_spinner)
        selection_layout.add_widget(second_layout)
        
        layout.add_widget(selection_layout)
        
        # Compare button
        compare_btn = Button(text='Compare', size_hint_y=None, height=50)
        compare_btn.bind(on_press=self.compare_cultures)
        layout.add_widget(compare_btn)
        
        # Results area
        self.results_label = Label(text='Select two cultures and press Compare', halign='left', valign='top')
        self.results_label.bind(
            texture_size=lambda obj, value: setattr(obj, 'text_size', (obj.width, None)),
            width=lambda obj, value: setattr(obj, 'text_size', (value, None)))
        
        scroll_view = ScrollView()
        scroll_view.add_widget(self.results_label)
        layout.add_widget(scroll_view)
        
        # Back button
        back_btn = Button(text='Back to List', size_hint_y=None, height=50)
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
    
    def compare_cultures(self, instance):
        """Compare the selected cultures"""
        first_culture = self.first_spinner.text
        second_culture = self.second_spinner.text
        
        if first_culture == 'Select Culture' or second_culture == 'Select Culture':
            self.results_label.text = 'Please select two cultures to compare'
            return
        
        comparison_text = f'Comparison: {first_culture.replace("_", " ")} vs {second_culture.replace("_", " ")}\n\n'
        comparison_text += 'This is a simplified comparison view.\n\n'
        comparison_text += f'First Culture: {first_culture}\n'
        comparison_text += f'Second Culture: {second_culture}\n\n'
        comparison_text += 'In a full implementation, this would show detailed comparisons\n'
        comparison_text += 'of values, innovations, social systems, and timelines.'
        
        self.results_label.text = comparison_text
    
    def go_back(self, instance):
        """Go back to the culture list"""
        self.manager.current = 'culture_list'


class CultureCodeApp(App):
    def build(self):
        # Set window size for better mobile simulation during development
        Window.size = (600, 900)
        
        # Create screen manager
        sm = ScreenManager()
        
        # Add screens
        culture_list_screen = CultureListScreen(sm, name='culture_list')
        culture_detail_screen = CultureDetailScreen(sm, name='culture_detail')
        compare_screen = CompareScreen(sm, name='compare')
        
        sm.add_widget(culture_list_screen)
        sm.add_widget(culture_detail_screen)
        sm.add_widget(compare_screen)
        
        # Set initial screen
        sm.current = 'culture_list'
        
        return sm


if __name__ == '__main__':
    CultureCodeApp().run()