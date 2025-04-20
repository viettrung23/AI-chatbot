import requests
from common.config import Config


def get_weather(city):
    config = Config()
    params = {
        "q": city,
        "appid": config.WEATHER_API_KEY,
        "units": "metric"
    }
    
    try:
        response = requests.get(config.WEATHER_API_URL, params=params)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        
        data = response.json()
        
        weather_info = {
            "city": data.get("name", city),
            "weather": {
                "description": data["weather"][0]["description"],
                "main": data["weather"][0]["main"]
            },
            "temperature": {
                "current": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "min": data["main"]["temp_min"],
                "max": data["main"]["temp_max"]
            },
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "status": "success"
        }
        
        return weather_info
    
    except requests.exceptions.RequestException as e:
        return {
            "city": city,
            "status": "error",
            "message": f"Unable to fetch weather data: {str(e)}"
        }
