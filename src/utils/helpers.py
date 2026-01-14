

from typing import Union

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit
    
    Args:
        celsius: Temperature in Celsius
        
    Returns:
        Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32

def format_temperature(temp: float, unit: str = 'celsius') -> str:
    """
    Format temperature with appropriate unit symbol
    
    Args:
        temp: Temperature value
        unit: 'celsius' or 'fahrenheit'
        
    Returns:
        Formatted temperature string
    """
    if unit.lower() == 'fahrenheit':
        temp = celsius_to_fahrenheit(temp)
        return f"{temp:.1f}°F"
    else:
        return f"{temp:.1f}°C"

def get_weather_icon(weather_condition: str) -> str:
    """
    Get emoji icon for weather condition
    
    Args:
        weather_condition: Weather condition name (e.g., 'Clear', 'Rain')
        
    Returns:
        Emoji icon string
    """
    icons = {
        'Clear': '☀️',
        'Clouds': '☁️',
        'Rain': '🌧️',
        'Drizzle': '🌦️',
        'Thunderstorm': '⛈️',
        'Snow': '❄️',
        'Mist': '🌫️',
        'Fog': '🌫️',
        'Haze': '🌫️',
        'Smoke': '💨',
    }
    return icons.get(weather_condition, '🌤️')

def validate_city_name(city: str) -> bool:
    """
    Validate city name input
    
    Args:
        city: City name to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not city or not city.strip():
        return False
    
    # Check if city name contains only valid characters
    # Allow letters, spaces, hyphens, and apostrophes
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'")
    return all(c in valid_chars for c in city)

def format_wind_speed(speed: float, unit: str = 'm/s') -> str:
    """
    Format wind speed with unit
    
    Args:
        speed: Wind speed value
        unit: Unit for wind speed
        
    Returns:
        Formatted wind speed string
    """
    if unit == 'mph':
        speed = speed * 2.237  # Convert m/s to mph
        return f"{speed:.1f} mph"
    elif unit == 'km/h':
        speed = speed * 3.6  # Convert m/s to km/h
        return f"{speed:.1f} km/h"
    else:
        return f"{speed:.1f} m/s"

def format_pressure(pressure: float) -> str:
    """
    Format atmospheric pressure
    
    Args:
        pressure: Pressure in hPa
        
    Returns:
        Formatted pressure string
    """
    return f"{pressure} hPa"

def get_time_of_day(timestamp: int) -> str:
    """
    Get time of day from timestamp
    
    Args:
        timestamp: Unix timestamp
        
    Returns:
        Time string in HH:MM format
    """
    from datetime import datetime
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%H:%M")