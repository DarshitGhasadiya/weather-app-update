import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class WeatherAppWindow:
    def __init__(self, root):
        self.root = root
        self.german_cities = [
            "Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne",
            "Stuttgart", "Düsseldorf", "Dortmund", "Essen", "Leipzig",
            "Bremen", "Dresden", "Hanover", "Nuremberg", "Duisburg",
            "Zwickau", "Zweibrücken"
        ]
        self.filtered_cities = self.german_cities.copy()
        
        # Weather emoji icons
        self.weather_icons = {
            'clear': '☀️',
            'sunny': '☀️',
            'clouds': '☁️',
            'cloudy': '☁️',
            'rain': '🌧️',
            'rainy': '🌧️',
            'snow': '❄️',
            'snowy': '❄️',
            'thunderstorm': '⛈️',
            'drizzle': '🌦️',
            'mist': '🌫️',
            'fog': '🌫️',
            'default': '🌤️'
        }
        
        self.setup_window()
        self.create_widgets()
    
    def setup_window(self):
        """Configure the main window properties"""
        self.root.title("Weather Forecast App")
        self.root.geometry("1400x800")
        self.root.minsize(1200, 700)
        
        # Center window on screen
        self.center_window()
        
        # Dark theme colors
        self.colors = {
            'bg_dark': '#1e1e2e',
            'bg_medium': '#2d2d44',
            'bg_light': '#3d3d5c',
            'sidebar_bg': '#252538',
            'accent': '#6366f1',
            'text_primary': '#ffffff',
            'text_secondary': '#b4b4c8',
            'card_bg': '#2d2d44'
        }
        
        # Configure root background
        self.root.configure(bg=self.colors['bg_dark'])
        
        # Make window responsive
        self.root.columnconfigure(0, weight=0)  # Sidebar
        self.root.columnconfigure(1, weight=1)  # Main content
        self.root.rowconfigure(0, weight=1)
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Create and layout all widgets"""
        # Left Sidebar
        self.create_sidebar()
        
        # Main Content Area
        self.create_main_content()
    
    def create_sidebar(self):
        """Create the left sidebar with city list"""
        sidebar = tk.Frame(self.root, bg=self.colors['sidebar_bg'], width=200)
        sidebar.grid(row=0, column=0, sticky='nsew', padx=15, pady=15)
        sidebar.grid_propagate(False)
        
        # Search Entry in Sidebar
        search_frame = tk.Frame(sidebar, bg=self.colors['sidebar_bg'])
        search_frame.pack(fill='x', padx=10, pady=(10, 20))
        
        self.sidebar_search = tk.Entry(
            search_frame,
            font=('Arial', 11),
            bg=self.colors['bg_light'],
            fg=self.colors['text_primary'],
            insertbackground='white',
            relief='flat',
            bd=0
        )
        self.sidebar_search.pack(fill='x', ipady=8, padx=5)
        self.sidebar_search.insert(0, "  🔍 Search city...")
        self.sidebar_search.bind('<KeyRelease>', self.filter_cities)
        self.sidebar_search.bind('<FocusIn>', self.on_sidebar_search_focus_in)
        self.sidebar_search.bind('<FocusOut>', self.on_sidebar_search_focus_out)
        
        # City List
        list_frame = tk.Frame(sidebar, bg=self.colors['sidebar_bg'])
        list_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.city_buttons = []
        self.populate_city_buttons(list_frame)
    
    def populate_city_buttons(self, parent):
        """Create city buttons in sidebar"""
        for city in self.german_cities:
            btn_frame = tk.Frame(parent, bg=self.colors['bg_light'], bd=0)
            btn_frame.pack(fill='x', pady=3)
            
            city_btn = tk.Button(
                btn_frame,
                text=f"{city}",
                font=('Arial', 11),
                bg=self.colors['bg_light'],
                fg=self.colors['text_primary'],
                activebackground=self.colors['accent'],
                activeforeground='white',
                relief='flat',
                bd=0,
                anchor='w',
                padx=15,
                pady=10,
                cursor='hand2',
                command=lambda c=city: self.load_weather_for_city(c)
            )
            city_btn.pack(fill='both')
            
            # Add weather icon and temp placeholder
            temp_label = tk.Label(
                btn_frame,
                text="21°",
                font=('Arial', 10),
                bg=self.colors['bg_light'],
                fg=self.colors['text_secondary']
            )
            temp_label.place(relx=0.85, rely=0.5, anchor='center')
            
            self.city_buttons.append((btn_frame, city_btn, temp_label, city))
    
    def create_main_content(self):
        """Create the main content area"""
        # Main container
        self.main_container = tk.Frame(self.root, bg=self.colors['bg_dark'])
        self.main_container.grid(row=0, column=1, sticky='nsew', padx=(0, 15), pady=15)
        self.main_container.columnconfigure(0, weight=1)
        self.main_container.rowconfigure(2, weight=1)
        
        # Current Weather Section
        self.create_current_weather_section()
        
        # Weather Details (Sunrise, Sunset, etc.)
        self.create_weather_details_section()
        
        # Hourly Forecast
        self.create_hourly_forecast_section()
    
    def create_current_weather_section(self):
        """Create current weather display"""
        current_frame = tk.Frame(self.main_container, bg=self.colors['bg_dark'])
        current_frame.grid(row=0, column=0, sticky='ew', pady=(0, 20))
        
        # City Name
        self.city_label = tk.Label(
            current_frame,
            text="Zwickau",
            font=('Arial', 36, 'bold'),
            bg=self.colors['bg_dark'],
            fg=self.colors['text_primary']
        )
        self.city_label.pack()
        
        # Temperature
        self.temp_label = tk.Label(
            current_frame,
            text="21°C",
            font=('Arial', 80, 'bold'),
            bg=self.colors['bg_dark'],
            fg=self.colors['text_primary']
        )
        self.temp_label.pack()
        
        # Weather Description
        self.description_label = tk.Label(
            current_frame,
            text="Rainy",
            font=('Arial', 20),
            bg=self.colors['bg_dark'],
            fg=self.colors['text_secondary']
        )
        self.description_label.pack()
    
    def create_weather_details_section(self):
        """Create weather details cards (Sunrise, Sunset, Visibility, UV Index)"""
        details_frame = tk.Frame(self.main_container, bg=self.colors['bg_dark'])
        details_frame.grid(row=1, column=0, sticky='ew', pady=(0, 20))
        
        # Create 4 detail cards
        details = [
            ("Sunrise", "☀️", "6:45 AM"),
            ("Sunset", "🌙", "8:49 AM"),
            ("Visibility", "👁️", "7 km"),
            ("UV Index", "☀️", "7 km")
        ]
        
        self.detail_cards = []
        for i, (title, icon, value) in enumerate(details):
            card = self.create_detail_card(details_frame, title, icon, value)
            card.pack(side='left', fill='both', expand=True, padx=5)
            self.detail_cards.append(card)
    
    def create_detail_card(self, parent, title, icon, value):
        """Create a single detail card"""
        card = tk.Frame(parent, bg=self.colors['card_bg'], bd=0)
        
        # Icon and Title
        header = tk.Frame(card, bg=self.colors['card_bg'])
        header.pack(fill='x', pady=(15, 5))
        
        icon_label = tk.Label(
            header,
            text=icon,
            font=('Arial', 20),
            bg=self.colors['card_bg']
        )
        icon_label.pack(side='left', padx=(15, 5))
        
        title_label = tk.Label(
            header,
            text=title,
            font=('Arial', 12),
            bg=self.colors['card_bg'],
            fg=self.colors['text_secondary']
        )
        title_label.pack(side='left')
        
        # Value
        value_label = tk.Label(
            card,
            text=value,
            font=('Arial', 16, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['text_primary']
        )
        value_label.pack(pady=(0, 15), padx=15, anchor='w')
        
        card.value_label = value_label
        return card
    
    def create_hourly_forecast_section(self):
        """Create hourly forecast section with horizontal scroll"""
        # Container
        forecast_container = tk.Frame(self.main_container, bg=self.colors['bg_dark'])
        forecast_container.grid(row=2, column=0, sticky='nsew')
        
        # Title
        title_label = tk.Label(
            forecast_container,
            text="Hourly Forecast",
            font=('Arial', 18, 'bold'),
            bg=self.colors['bg_dark'],
            fg=self.colors['text_primary'],
            anchor='w'
        )
        title_label.pack(fill='x', pady=(0, 15))
        
        # Scrollable frame
        canvas = tk.Canvas(
            forecast_container,
            bg=self.colors['bg_medium'],
            highlightthickness=0,
            height=280
        )
        canvas.pack(fill='both', expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(
            forecast_container,
            orient='horizontal',
            command=canvas.xview
        )
        scrollbar.pack(fill='x')
        canvas.configure(xscrollcommand=scrollbar.set)
        
        # Frame inside canvas
        hourly_frame = tk.Frame(canvas, bg=self.colors['bg_medium'])
        canvas.create_window((0, 0), window=hourly_frame, anchor='nw')
        
        # Create 24 hourly cards
        self.hourly_cards = []
        hours_data = [
            ("06", "☁️", "21°"),
            ("07", "☁️", "23°"),
            ("08", "🌧️", "25°"),
            ("09", "🌧️", "27°"),
            ("10", "🌧️", "25°"),
            ("11", "🌦️", "30°"),
            ("12", "☀️", "31°"),
            ("13", "☀️", "32°"),
            ("14", "☀️", "33°"),
            ("15", "☀️", "34°"),
            ("16", "🌤️", "35°"),
            ("17", "🌤️", "37°"),
            ("18", "🌤️", "38°"),
            ("19", "🌤️", "35°"),
        ]
        
        for i, (hour, icon, temp) in enumerate(hours_data):
            card = self.create_hourly_card(hourly_frame, hour, icon, temp)
            card.pack(side='left', padx=5, pady=10)
            self.hourly_cards.append(card)
        
        # Update scroll region
        hourly_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'))
    
    def create_hourly_card(self, parent, hour, icon, temp):
        """Create a single hourly forecast card"""
        card = tk.Frame(parent, bg=self.colors['card_bg'], width=80, height=200)
        card.pack_propagate(False)
        
        # Time
        time_label = tk.Label(
            card,
            text=f"{hour}:00",
            font=('Arial', 12),
            bg=self.colors['card_bg'],
            fg=self.colors['text_secondary']
        )
        time_label.pack(pady=(20, 10))
        
        # Weather Icon
        icon_label = tk.Label(
            card,
            text=icon,
            font=('Arial', 30),
            bg=self.colors['card_bg']
        )
        icon_label.pack(pady=10)
        
        # Temperature
        temp_label = tk.Label(
            card,
            text=temp,
            font=('Arial', 16, 'bold'),
            bg=self.colors['card_bg'],
            fg=self.colors['text_primary']
        )
        temp_label.pack(pady=(10, 20))
        
        card.temp_label = temp_label
        card.icon_label = icon_label
        return card
    
    def filter_cities(self, event=None):
        """Filter cities based on search input"""
        search_term = self.sidebar_search.get().replace("  🔍 Search city...", "").strip().lower()
        
        # Show/hide city buttons based on search
        for btn_frame, city_btn, temp_label, city in self.city_buttons:
            if search_term in city.lower() or search_term == "":
                btn_frame.pack(fill='x', pady=3)
            else:
                btn_frame.pack_forget()
    
    def on_sidebar_search_focus_in(self, event):
        """Clear placeholder text on focus"""
        if self.sidebar_search.get() == "  🔍 Search city...":
            self.sidebar_search.delete(0, tk.END)
    
    def on_sidebar_search_focus_out(self, event):
        """Restore placeholder if empty"""
        if not self.sidebar_search.get():
            self.sidebar_search.insert(0, "  🔍 Search city...")
    
    def load_weather_for_city(self, city):
        """Load weather data for selected city"""
        print(f"Loading weather for: {city}")
        self.city_label.config(text=city)
        # This will be connected to your weather API later
    
    def get_weather_icon(self, condition):
        """Get emoji icon for weather condition"""
        condition_lower = condition.lower()
        for key in self.weather_icons:
            if key in condition_lower:
                return self.weather_icons[key]
        return self.weather_icons['default']
    
    def update_current_weather(self, weather_data):
        """Update current weather display"""
        self.city_label.config(text=weather_data.get('city', 'Unknown'))
        self.temp_label.config(text=f"{weather_data.get('temp', '--')}°C")
        
        description = weather_data.get('description', 'No data')
        icon = self.get_weather_icon(description)
        self.description_label.config(text=f"{icon} {description}")
    
    def update_weather_details(self, details_data):
        """Update weather detail cards"""
        # Sunrise
        self.detail_cards[0].value_label.config(text=details_data.get('sunrise', '--'))
        # Sunset
        self.detail_cards[1].value_label.config(text=details_data.get('sunset', '--'))
        # Visibility
        self.detail_cards[2].value_label.config(text=f"{details_data.get('visibility', '--')} km")
        # UV Index
        self.detail_cards[3].value_label.config(text=details_data.get('uv_index', '--'))
    
    def update_hourly_forecast(self, hourly_data):
        """Update hourly forecast display"""
        for i, card in enumerate(self.hourly_cards):
            if i < len(hourly_data):
                hour_data = hourly_data[i]
                card.temp_label.config(text=f"{hour_data.get('temp', '--')}°")
                icon = self.get_weather_icon(hour_data.get('description', ''))
                card.icon_label.config(text=icon)


def create_main_window():
    """Create and return the main application window"""
    root = tk.Tk()
    app = WeatherAppWindow(root)
    return root, app