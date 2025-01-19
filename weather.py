import os
from pprint import pprint
from dotenv import load_dotenv
import requests


# loads the environment variables
load_dotenv()


def get_current_weather(city="Dublin", country_code="IE"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city},{country_code}&units=metric"

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***")
    city = input("\nPlease enter a city name: ")

    # check for empty string or string with only spaces
    if not bool(city.strip()):  # bool() is like an existence/null check
        city = "Kansas City"

    country = input("\nPlease enter a 2-letter country code: ")

    # check for empty string or string with only spaces
    if not bool(country.strip()):  # bool() is like an existence/null check
        country = "US"

    weather_data = get_current_weather(city, country)

    print("\n")
    pprint(weather_data)
