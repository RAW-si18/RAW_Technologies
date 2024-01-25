# Updated 23/1/24

import requests
from raw_modules.speak_func import speak
from raw_modules.city_name import city_name_function
api_key_weather = 'dae16e1806b96eda34fedfd26f60505c'

def get_weather(city='Ahmedabad') -> None:
    '''climate condition using api'''
    city_properties=city_name_function(city)
    if city_properties==None:
        return
    city=city_properties[0]+','+city_properties[4]
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key_weather,
        "units": "metric", 
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather_description = data.get('weather', [{}])[0].get('description', 'N/A')
            temperature = data.get('main', {}).get('temp', 'N/A')
            humidity = data.get('main', {}).get('humidity', 'N/A')
            wind_speed = data.get('wind', {}).get('speed', 'N/A')
            print(f"\nWeather in {city}: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s\n")
            speak(f"Weather in {city} is {weather_description}, that is {temperature} degree celsius and {humidity}% humidity with a wind speed of {wind_speed} metre per second.")
        else:
            print(f"Error: {data.get('message', 'No detailed error message available')}")
    except Exception as e:
        print(f"An error occurred: {e}")
