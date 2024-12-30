# API code
from dotenv import load_dotenv
import dearpygui.dearpygui as dpg
import os
import datetime
import requests
from geopy.geocoders import Nominatim
load_dotenv('api.env')

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
def fetch_weather(sender, data):
    city = dpg.get_value("City Name")
    city = str(city).title()
    
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
    lat = geo[0]
    lon = geo[1]
    dpg.set_value("latlon","City:" + city)
    dpg.set_value("Weather_Conditions","")
    
    BASE_URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units={unitvalue}"
    print(BASE_URL)
    try:
        response = requests.get(BASE_URL)
        weather_data = response.json()
        output = ""
        weather_conditions = []
        # Extracting required weather details
        for i in range(0,40):
            temp = weather_data["list"][i]["main"]["temp"]
            dt = weather_data["list"][i]["dt"]
            weather_desc = weather_data["list"][i]["weather"][0]["description"]
            humidity = weather_data["list"][i]["main"]["humidity"]
            wind_speed = weather_data["list"][i]["wind"]["speed"]
            degrees = weather_data["list"][i]["wind"]["deg"]
            date_time = datetime.datetime.utcfromtimestamp(dt) 
            # Formatting output
            if unitvalue =="metric":
                # output += (f"City: {city}\n"
                #         f"Date {date_time}\n"
                #         f"Temperature: {temp}°C\n"
                #         f"Condition: {weather_desc}\n"
                #         f"Humidity: {humidity}%\n"
                #         f"Wind Speed: {wind_speed} m/s\n"
                #         f"Degrees: {degrees}°\n")
                weather_conditions.append(f"DateTime: {date_time} Temp: {temp}°C Condition: {weather_desc} Humidity: {humidity}% Wind: {wind_speed} m/s Degrees: {degrees}°")
            elif unitvalue == "imperial":
                
                # output += (f"City: {city}\n"
                #         f"Date {date_time}\n"
                #         f"Temperature: {temp}°F\n"
                #         f"Condition: {weather_desc}\n"
                #         f"Humidity: {humidity}%\n"
                #         f"Wind Speed: {wind_speed} m/s\n"
                #         f"Degrees: {degrees}°\n")
                weather_conditions.append(f"DateTime: {date_time} Temp: {temp}°F Condition: {weather_desc} Humidity: {humidity}% Wind: {wind_speed} mph Degrees: {degrees}°")

        
            elif unitvalue == "kelvin":
                weather_conditions.append(f"DateTime: {date_time} Temp: {temp}°K Condition: {weather_desc} Humidity: {humidity}% Wind: {wind_speed} m/s Degrees: {degrees}°")

        
                # output += (f"City: {city}\n"
                #         f"Date {date_time}\n"
                #         f"Temperature: {temp}°K\n"
                #         f"Condition: {weather_desc}\n"
                #         f"Humidity: {humidity}%\n"
                #         f"Wind Speed: {wind_speed} m/s\n"
                #         f"Degrees: {degrees}°\n")
        dpg.configure_item("Weather_Conditions", items=weather_conditions)
    except Exception as e:
        dpg.set_value("Weather Output", f"Error: {str(e)}")
        print(e) 

# city to lat long using Nominatim API 
def city_to_lat_lon(city_name):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(city_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

    latitude, longitude = city_to_lat_lon(city_name)
    if latitude and longitude:
        print(f"The coordinates of {city} are: Latitude = {latitude}, Longitude = {longitude}")
    else:
        print(f"Could not find coordinates for {city}")