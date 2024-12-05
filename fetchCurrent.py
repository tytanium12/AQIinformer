import requests
import pandas as pd
from datetime import datetime, timezone
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz

# Class that fetches and calculates important information (AQI, AQI color code, weather, time, city from coordinates)
class Fetch:
    def __init__(self, latitude, longitude):
        # Initialize with location coordinates
        self.latitude = latitude
        self.longitude = longitude

    def fetch_aqi_data(self):
        # Fetches AQI data from the Open-Meteo API and returns it as a pandas DataFrame.
        url = "https://air-quality-api.open-meteo.com/v1/air-quality"
        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "hourly": ["us_aqi"],
            "past_days": 3,
            "forecast_days": 3
        }
        response = requests.get(url, params=params)
        data = response.json()

        # Convert time and AQI data to a DataFrame
        hourly = data['hourly']
        df = pd.DataFrame({
            'time': pd.to_datetime(hourly['time']),
            'us_aqi': hourly['us_aqi']
        })

        return df

    def get_aqi_color(self, aqi):
        # Returns the color code based on AQI severity.
        if 0 <= aqi <= 50:
            return "#00e400" # green
        elif 51 <= aqi <= 100:
            return "#ffff00" # yellow
        elif 101 <= aqi <= 150:
            return "#ff7e00" # orange
        elif 151 <= aqi <= 200:
            return "#ff0000" # red
        elif 201 <= aqi <= 300:
            return "#8f3f97" # purple
        else:
            return "#7e0023" # maroon

    def fetch_weather_data(self):
        # Fetches weather data from the Open-Meteo API and returns it as a pandas DataFrame.
        try:
            url = "https://api.open-meteo.com/v1/forecast"
            params = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
                "past_hours": 24,
                "forecast_days": 1,
                "temperature_unit": "fahrenheit",
                "wind_speed_unit": "mph",
                "precipitation_unit": "inch",
            }
            response = requests.get(url, params=params)
            response.raise_for_status()  # Check for errors
            data = response.json()

            # Extract and format data
            hourly = data['hourly']
            df = pd.DataFrame({
                'time': pd.to_datetime(hourly['time']),
                'temperature_2m': hourly['temperature_2m'],
                'precipitation': hourly['precipitation'],
                'wind_speed_10m': hourly['wind_speed_10m']
            })

            return df
        except Exception as e:
            return f"Error fetching weather data: {e}"

    def fetch_rounded_time(self):
        time_now_GMT = datetime.now(timezone.utc)
        time_now_str = time_now_GMT.strftime("%Y-%m-%d %H:%M:%S")
        time_now_GMT_datetime = datetime.strptime(time_now_str, "%Y-%m-%d %H:%M:%S")
        rounded_time = time_now_GMT_datetime.replace(minute=0, second=0, microsecond=0)
        return rounded_time

    def get_city_from_coordinates(self, lat, lon):
        # Initialize the geolocator
        geolocator = Nominatim(user_agent="friends_of_aqiInformer_app")

        # Create the coordinates string
        coordinates = f"{lat}, {lon}"

        # Get location information
        location = geolocator.reverse(coordinates, exactly_one=True)

        # Extract and return the city if available
        if location and "city" in location.raw['address']:
            return location.raw['address']['city']
        elif location and "town" in location.raw['address']:
            return location.raw['address']['town']
        elif location and "village" in location.raw['address']:
            return location.raw['address']['village']
        else:
            return "City not found"

    def get_local_time(self, lat, lon):
        # Initialize TimezoneFinder
        tf = TimezoneFinder()

        # Find the timezone name based on latitude and longitude
        timezone_str = tf.timezone_at(lat=lat, lng=lon)

        if timezone_str:
            # Get the timezone object
            timezone = pytz.timezone(timezone_str)

            # Get the current time in that timezone
            current_time = datetime.now(timezone)

            # Return the timezone name and current time in that timezone
            return current_time#, timezone
        else:
            return "Timezone not found"#, None