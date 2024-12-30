# API code
from dotenv import load_dotenv
import dearpygui.dearpygui as dpg
import os
import time
import requests
from geopy.geocoders import Nominatim
load_dotenv('api.env')

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
def fetch_weather(sender, data):
    city = dpg.get_value("City Name")
    unitvalue = dpg.get_value("Measurement")
    print(unitvalue)
    print(city)
    geo = city_to_lat_lon(city)
    print(geo)
    if not city:
        dpg.set_value("Weather Output", "Please enter a city name.")
        return
    if not geo:
        dpg.set_value("Weather Output", "Please enter a valid city name.")
        return
   
    
    BASE_URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units={unitvalue}"
    print(BASE_URL)
    try:
        response = requests.get(BASE_URL)
        weather_data = response.json()
        
        print(weather_data["list"][1])
        print(weather_data["list"][1]["main"])

        # Extracting required weather details
        temp = weather_data["list"][1]["main"]["temp"]
        print(temp)
        weather_desc = weather_data["list"][1]["weather"][0]["description"]
        humidity = weather_data["list"][1]["main"]["humidity"]
        wind_speed = weather_data["list"][1]["wind"]["speed"]
        degrees = weather_data["list"][1]["wind"]["deg"]
        print(temp)
        # Formatting output
        if unitvalue =="metric":
            output = (f"City: {city}\n"
                    f"Temperature: {temp}°C\n"
                    f"Condition: {weather_desc}\n"
                    f"Humidity: {humidity}%\n"
                    f"Wind Speed: {wind_speed} m/s\n"
                    f"Degrees: {degrees}°\n")
        else:
            
            output = (f"City: {city}\n"
                    f"Temperature: {temp}°F\n"
                    f"Condition: {weather_desc}\n"
                    f"Humidity: {humidity}%\n"
                    f"Wind Speed: {wind_speed} m/s\n"
                    f"Degrees: {degrees}°\n")
        dpg.set_value("Weather Output", output)
    except Exception as e:
        dpg.set_value("Weather Output", f"Error: {str(e)}")
        print(e) 

def city_to_lat_lon(city_name):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Example usage

    latitude, longitude = city_to_lat_lon(city_name)
    if latitude and longitude:
        print(f"The coordinates of {city} are: Latitude = {latitude}, Longitude = {longitude}")
    else:
        print(f"Could not find coordinates for {city}")