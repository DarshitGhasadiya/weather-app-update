"""
Configuration constants for the Weather App
"""

# ============================================================================
# WINDOW CONFIGURATION
# ============================================================================

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
WINDOW_TITLE = 'Weather App'
RESIZABLE = False

# ============================================================================
# API CONFIGURATION
# ============================================================================

API_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = '4cec456a12e78e190dc12413b1d46585'

# ============================================================================
# FONT CONFIGURATION
# ============================================================================

FONT_TITLE = ('Time New Roman', 30, 'bold')
FONT_LABEL = ('Time New Roman', 20)
FONT_LABEL_SMALL = ('Time New Roman', 16)
FONT_BUTTON = ('Time New Roman', 20, 'bold')
FONT_DROPDOWN = ('Time New Roman', 25, 'bold')

# ============================================================================
# COLOR CONFIGURATION
# ============================================================================

HEADER_BG = 'skyblue'
SELECTOR_BG = 'yellow'

# ============================================================================
# CITY DATA
# ============================================================================

CITY_LIST = ["Zwickau", "Zurich", "Tbilisi"]

# ============================================================================
# UI POSITIONS AND DIMENSIONS
# ============================================================================

# Header
HEADER_X = 25
HEADER_Y = 40
HEADER_WIDTH = 625
HEADER_HEIGHT = 40

# City Selector
SELECTOR_X = 25
SELECTOR_Y = 100
SELECTOR_WIDTH = 450
SELECTOR_HEIGHT = 40
SELECTOR_LABEL_X = 500
SELECTOR_LABEL_WIDTH = 148

# Weather Display
WEATHER_DISPLAY_START_Y = 210
WEATHER_DISPLAY_Y_OFFSET = 45
LABEL_X = 30
VALUE_X = 250
DISPLAY_WIDTH = 200
DISPLAY_HEIGHT = 30

# Button
BUTTON_X = 200
BUTTON_Y = 150
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 50

# Footer
FOOTER_X = 30
FOOTER_Y = 400
FOOTER_WIDTH = 420
FOOTER_HEIGHT = 30
