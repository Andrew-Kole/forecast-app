import typing
from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY: typing.Final = os.getenv("API_KEY")

def get_data(place, forecast_days, kind=None):
    url = "http://api.openweathermap.org/data/2.5/forecast"
    r = requests.get(url, params={"q": place, "appid": API_KEY})
    data = r.json()
    filtered_data = data["list"]
    nr_values = forecast_days * 8
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data



if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Sky"))