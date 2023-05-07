import typing
from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY: typing.Final = os.getenv("API_KEY")

def get_data(place, forecast_days):
    url = "http://api.openweathermap.org/data/2.5/forecast"
    r = requests.get(url, params={"q": place, "appid": API_KEY})
    data = r.json()
    filtered_data = data["list"]
    nr_values = forecast_days * 8
    filtered_data = filtered_data[:nr_values]
    return filtered_data



if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))