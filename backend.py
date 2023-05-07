import typing
from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY: typing.Final = os.getenv("API_KEY")

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    r = requests.get(url)
    data = r.json()
    return data


if __name__ == "__main__":
    print(get_data(place="Tokyo"))