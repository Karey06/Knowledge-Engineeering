# Weather API code used in Autonomous_Trailer.ipynb (Step 2 and Step 4)
# API: Open-Meteo - https://open-meteo.com/ (free, no API key needed)

import requests

town_location = {
    'Nairobi': (-1.29, 36.82),
    'Nakuru': (-0.30, 36.07),
    'Kericho': (-0.37, 35.28),
    'Kisii': (-0.68, 34.77),
    'Eldoret': (0.51, 35.27),
    'Kakamega': (0.28, 34.75),
    'Kisumu': (-0.09, 34.77)
}

def get_weather(town):
    lat, lon = town_location[town]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        data = requests.get(url, timeout=5).json()
        code = data["current_weather"]["weathercode"]
        # weather codes: 45 and 48 = fog, 51 and above = rain/drizzle/storm
        if code in [45, 48]:
            return "Fog"
        elif code >= 51:
            return "Rain"
        else:
            return "Clear"
    except:
        return "Clear"   # if there is no internet, assume clear

for town in town_location:
    print(town, ":", get_weather(town))
