import requests
import os

def oslo():
    api_nokkel = os.getenv("OPENWEATHER_API_KEY")

    if not api_nokkel:
        print("Mangler API-nøkkel")
        return

    svar = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "q": "Oslo,no",
            "appid": api_nokkel,
            "units": "metric"
        }
    )

    temperatur = svar.json()["main"]["temp"]
    print("Temperatur i Oslo:", temperatur, "°C")
